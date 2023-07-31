from setuptools import setup, Extension

# Define the C extension module
c_extension = Extension(
    'your_package.c_module', # The name of the C extension module
    sources=['./run.c'],
    # Add any other compilation options if needed (e.g., include_dirs, extra_compile_args)
)

# Setup the Python package
setup(
    name='llamac2py',
    author='Adarsh Shirawalmath',
    version='0.1',
    description="llamac2py is a Python package that provides a wrapper for running inference using the Llama-2 Transformer model. The package includes a C executable (run.c) from Karpathy's llama2.c that performs the inference, and the wrapper module (wrapper.py) allows easy integration of the C code into Python scripts.",
    packages=[],
    ext_modules=[c_extension],  # Include the C extension module
)
