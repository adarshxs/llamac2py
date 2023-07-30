# llamac2python

Compile the C code using the following command to generate the executable "run" using:
`make run`

Then:

```
from llamac2py.wrapper import generate_short_story

# Load your Llama-2 model checkpoint (model.bin) here
checkpoint_file = 'path/to/your/model.bin'

# Generate a short story with a prompt
prompt_text = "Once upon a time, in a faraway land,"
short_story = generate_short_story(prompt_text, checkpoint_file)
print(short_story)
```