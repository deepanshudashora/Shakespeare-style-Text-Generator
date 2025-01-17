# Shakespeare-style Text Generator

This project uses a GPT-based model to generate text in the style of Shakespeare. The model is trained on a dataset of Shakespeare's works and can generate text based on a given prompt.

## Features

- Generate text in the style of Shakespeare.
- Adjustable parameters for text generation, including max length, temperature, top-k sampling, and number of samples.
- Gradio interface for easy interaction.

## Training Logs

```
didn't crash yet!
> Hello, I'm a language model, not a program.

So this morning I started studying for the interview in the lab. This was not
> Hello, I'm a language model, and one of the main things that bothers me when they create languages is how easy it becomes to create something that
> Hello, I'm a language model, and I wrote it off on the grounds that a language model would make me more fluent. But I'm not
> Hello, I'm a language model, I really like languages. I like languages because like, they're good. And the way we talk about languages
> Hello, I'm a language model, a language model I'm using for data modelling. All I did was test the results and then I wrote some
Model Parameters (name and shape):
Total Parameters: 162.35M
step 0: loss 0.2199, lr 0.000000
New best loss: 0.2199 - Saving model...
step 100: loss 8.6011, lr 0.000005
step 200: loss 8.3040, lr 0.000010
step 300: loss 7.2572, lr 0.000015
step 400: loss 6.3143, lr 0.000020
step 500: loss 5.6861, lr 0.000025
step 600: loss 5.2858, lr 0.000030
step 700: loss 5.0145, lr 0.000035
step 800: loss 4.8127, lr 0.000040
step 900: loss 4.6757, lr 0.000045
step 1000: loss 4.5286, lr 0.000050
step 1100: loss 4.4477, lr 0.000055
step 1200: loss 4.3364, lr 0.000060
step 1300: loss 4.2295, lr 0.000065
step 1400: loss 4.1212, lr 0.000070
step 1500: loss 4.0399, lr 0.000075
step 1600: loss 3.9334, lr 0.000080
step 1700: loss 3.8221, lr 0.000085
step 1800: loss 3.7355, lr 0.000090
step 1900: loss 3.6491, lr 0.000095
step 2000: loss 3.5456, lr 0.000100
step 2100: loss 3.4397, lr 0.000100
step 2200: loss 3.3379, lr 0.000100
step 2300: loss 3.2295, lr 0.000100
step 2400: loss 3.1348, lr 0.000100
step 2500: loss 2.9991, lr 0.000100
step 2600: loss 2.8419, lr 0.000100
step 2700: loss 2.7209, lr 0.000100
step 2800: loss 2.5794, lr 0.000100
step 2900: loss 2.4247, lr 0.000100
step 3000: loss 2.2492, lr 0.000100
step 3100: loss 2.0794, lr 0.000099
step 3200: loss 1.9038, lr 0.000099
step 3300: loss 1.7628, lr 0.000099
step 3400: loss 1.5719, lr 0.000099
step 3500: loss 1.4208, lr 0.000099
step 3600: loss 1.2720, lr 0.000099
step 3700: loss 1.1486, lr 0.000099
step 3800: loss 1.0083, lr 0.000099
step 3900: loss 0.8787, lr 0.000098
step 4000: loss 0.7605, lr 0.000098
step 4100: loss 0.6547, lr 0.000098
step 4200: loss 0.5852, lr 0.000098
step 4300: loss 0.5152, lr 0.000098
step 4400: loss 0.4507, lr 0.000098
step 4500: loss 0.4150, lr 0.000097
step 4600: loss 0.3771, lr 0.000097
step 4700: loss 0.3479, lr 0.000097
step 4800: loss 0.3223, lr 0.000097
step 4900: loss 0.3023, lr 0.000097
step 5000: loss 0.2877, lr 0.000096
step 5100: loss 0.2756, lr 0.000096
step 5200: loss 0.2644, lr 0.000096
step 5300: loss 0.2561, lr 0.000096
step 5400: loss 0.2455, lr 0.000095
step 5500: loss 0.2358, lr 0.000095
step 5600: loss 0.2287, lr 0.000095
step 5700: loss 0.2229, lr 0.000094
step 5800: loss 0.2170, lr 0.000094
New best loss: 0.2170 - Saving model...
step 5900: loss 0.2124, lr 0.000094
New best loss: 0.2124 - Saving model...
step 6000: loss 0.2092, lr 0.000093
New best loss: 0.2092 - Saving model...
step 6100: loss 0.2020, lr 0.000093
New best loss: 0.2020 - Saving model...
step 6200: loss 0.1983, lr 0.000093
New best loss: 0.1983 - Saving model...
step 6300: loss 0.1927, lr 0.000092
New best loss: 0.1927 - Saving model...
step 6400: loss 0.1905, lr 0.000092
New best loss: 0.1905 - Saving model...
step 6500: loss 0.1877, lr 0.000092
New best loss: 0.1877 - Saving model...
step 6600: loss 0.1853, lr 0.000091
New best loss: 0.1853 - Saving model...
step 6700: loss 0.1800, lr 0.000091
New best loss: 0.1800 - Saving model...
step 6800: loss 0.1781, lr 0.000091
New best loss: 0.1781 - Saving model...
step 6900: loss 0.1754, lr 0.000090
New best loss: 0.1754 - Saving model...
step 7000: loss 0.1723, lr 0.000090
New best loss: 0.1723 - Saving model...
step 7100: loss 0.1694, lr 0.000090
New best loss: 0.1694 - Saving model...
step 7200: loss 0.1670, lr 0.000089
New best loss: 0.1670 - Saving model...
step 7300: loss 0.1644, lr 0.000089
New best loss: 0.1644 - Saving model...
step 7400: loss 0.1625, lr 0.000088
New best loss: 0.1625 - Saving model...
step 7500: loss 0.1614, lr 0.000088
New best loss: 0.1614 - Saving model...
step 7600: loss 0.1593, lr 0.000087
New best loss: 0.1593 - Saving model...
step 7700: loss 0.1575, lr 0.000087
New best loss: 0.1575 - Saving model...
step 7800: loss 0.1564, lr 0.000087
New best loss: 0.1564 - Saving model...
step 7900: loss 0.1524, lr 0.000086
New best loss: 0.1524 - Saving model...
```

## Usage

To run the text generator, execute the `app.py` script. You can interact with the model through the Gradio interface.

## Requirements

- Python 3.x
- PyTorch
- Gradio
- tiktoken
- transformers

Install the required packages using:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.
