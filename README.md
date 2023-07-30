# llamac2py

llamac2py is a Python package that provides a wrapper for running inference using the Llama-2 Transformer model. The package includes a C executable (run.c) from [Karpathy's llama2.c](https://github.com/karpathy/llama2.c) that performs the inference, and the package allows easy inference for the same.
---
## Get Started:

Clone the Repository: `git clone https://github.com/adarshxs/llamac2py`

cd into the Repository: `cd llamac2py`

download the Model (Will add support for more models): 

`wget https://huggingface.co/karpathy/tinyllamas/resolve/main/stories15M.bin`

Compile the C file: `run make`

Then in a notebook or a Python script, run:

```
from llamac2py.wrapper import generate_short_story

# Load your Llama-2 model checkpoint (model.bin) here
checkpoint_file = 'path/to/your/model.bin'

# Generate a short story with a prompt
prompt_text = "Once upon a time, in a faraway land,"
short_story = generate_short_story(prompt_text, checkpoint_file)
print(short_story)
```
