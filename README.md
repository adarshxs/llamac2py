# llamac2python

llamac2py is a Python package that provides a wrapper for running inference using the Llama-2 Transformer model. The package includes a C executable (run.c) from Karpathy's llama2.c that performs the inference, and the wrapper module (wrapper.py) allows easy integration of the C code into Python scripts.
---
download model: 

`wget https://huggingface.co/karpathy/tinyllamas/resolve/main/stories15M.bin` # Will add support for more models

`git clone https://github.com/adarshxs/llamac2py`

Compile the C code using the following command to generate the executable "run" using:

`cd llamac2python && make run`


`cd .. ` # Go back to the root

Then in a notebook or a python script, run:

```
from llamac2py.wrapper import generate_short_story

# Load your Llama-2 model checkpoint (model.bin) here
checkpoint_file = 'path/to/your/model.bin'

# Generate a short story with a prompt
prompt_text = "Once upon a time, in a faraway land,"
short_story = generate_short_story(prompt_text, checkpoint_file)
print(short_story)
```
