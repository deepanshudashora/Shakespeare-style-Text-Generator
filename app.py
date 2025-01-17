import gradio as gr
import torch
import torch.nn as nn
from torch.nn import functional as F
import tiktoken

# Import the model architecture
from train_get2_1 import GPT, GPTConfig

# Model configuration and initialization
def init_model():
    config = GPTConfig(
        block_size=128,  # Match training block size
        vocab_size=50257,  # GPT-2 vocab size
        n_layer=12,
        n_head=12,
        n_embd=768
    )
    model = GPT(config)
    
    # Load the trained weights
    try:
        checkpoint = torch.load('shakespeare_model.pt')
        model.load_state_dict(checkpoint['model_state_dict'])
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Could not load model weights: {e}. Using base model.")
    
    model.eval()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = model.to(device)
    return model, device

# Initialize tokenizer and model
enc = tiktoken.get_encoding("gpt2")
model, device = init_model()

def generate_text(prompt, max_length=100, temperature=0.8, top_k=50, num_samples=3):
    """
    Generate text based on the prompt
    Args:
        prompt (str): Input text prompt
        max_length (int): Maximum length of generated text
        temperature (float): Controls randomness (higher = more random)
        top_k (int): Number of top tokens to consider for sampling
        num_samples (int): Number of different outputs to generate
    """
    # Encode the prompt
    tokens = torch.tensor(enc.encode(prompt), dtype=torch.long)
    tokens = tokens.unsqueeze(0).repeat(num_samples, 1)
    tokens = tokens.to(device)
    
    # Set model to eval mode
    model.eval()
    
    # Generate text
    with torch.no_grad():
        for _ in range(max_length):
            # Only use the last block_size tokens if input is too long
            idx_cond = tokens if tokens.size(1) <= model.config.block_size else tokens[:, -model.config.block_size:]
            
            # Get predictions
            logits = model(idx_cond)[0][:, -1, :] / temperature
            
            # Apply top-k sampling
            if top_k is not None:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = float('-inf')
            
            # Apply softmax and sample
            probs = F.softmax(logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)
            
            # Append to the sequence
            tokens = torch.cat((tokens, next_token), dim=1)
    
    # Decode and format the generated texts
    generated_texts = []
    for i in range(num_samples):
        text = enc.decode(tokens[i].tolist())
        generated_texts.append(f"Generation {i+1}:\n{text}\n")
    
    return "\n".join(generated_texts)

# Create the Gradio interface
demo = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(label="Enter your prompt", placeholder="Enter text here...", lines=3),
        gr.Slider(minimum=10, maximum=200, value=100, step=1, label="Max Length"),
        gr.Slider(minimum=0.1, maximum=2.0, value=0.8, step=0.1, label="Temperature"),
        gr.Slider(minimum=1, maximum=100, value=50, step=1, label="Top-k"),
        gr.Slider(minimum=1, maximum=5, value=3, step=1, label="Number of Samples")
    ],
    outputs=gr.Textbox(label="Generated Text", lines=10),
    title="Shakespeare-style Text Generator",
    description="Generate Shakespeare-style text based on your prompt. Higher temperature means more creative but potentially less coherent output.",
    examples=[
        ["ROMEO:", 100, 0.8, 50, 3],
        ["JULIET: My love,", 100, 0.8, 50, 3],
        ["HAMLET: To be, or not to be,", 100, 0.8, 50, 3],
        ["MACBETH: Is this a dagger", 100, 0.8, 50, 3]
    ]
)

if __name__ == "__main__":
    demo.launch()