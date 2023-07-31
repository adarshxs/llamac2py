# llamac2py

llamac2py is a Python package that provides a wrapper for running inference using the Llama-2 Transformer model. The package includes a C executable (run.c) from [Karpathy's llama2.c](https://github.com/karpathy/llama2.c) that performs the inference, and the package allows easy inference for the same.
---
![llama-cutie](https://github.com/adarshxs/llamac2py/assets/114558126/15968744-e623-4f45-81aa-a447a11860e8)
---
Note:
On Windows, use build_msvc.bat in a Visual Studio Command Prompt to build with msvc, or you can use make win64 to use mingw compiler toolchain from linux or windows to build the windows target. MSVC build will automatically use openmp and max threads appropriate for your CPU unless you set OMP_NUM_THREADS env.

On Centos 7, Amazon Linux 2018 use rungnu Makefile target: make rungnu or make runompgnu to use openmp.

## Get Started:

Clone the Repository: `git clone https://github.com/adarshxs/llamac2py`

cd into the Repository: `cd llamac2py`

download the Model (Will add support for more models): 

`wget https://huggingface.co/karpathy/tinyllamas/resolve/main/stories15M.bin`

Compile the C file: `make run`

Then in a notebook or a Python script, run:

```
from llamac2py.wrapper import generate_short_story

# Load your Llama-2 model checkpoint (model.bin) here
checkpoint_file = 'stories15M.bin'

# Generate a short story with a prompt
prompt_text = "Once upon a time, in a faraway land,"
short_story = generate_short_story(prompt_text, checkpoint_file)
print(short_story)
```
