from setuptools import setup, Extension
import platform

# Define the C extension module
c_extension = Extension(
    'llamac2py._c_module',  # The name of the C extension module
    sources=['llamac2py/run.c'],
    # Add any other compilation options if needed (e.g., include_dirs, extra_compile_args)
)

# Setup the Python package
setup(
    name='llamac2py',
    author='Adarsh Shirawalmath',
    version='0.1',
    description="llamac2py is a Python package that provides a wrapper for running inference using the Llama-2 Transformer model. The package includes a C executable (run.c) from Karpathy's llama2.c that performs the inference, and the wrapper module (wrapper.py) allows easy integration of the C code into Python scripts.",
    packages=['llamac2py'],  # Include the Python package(s)
    ext_modules=[c_extension],  # Include the C extension module
)

# Add platform-specific settings for Windows and MinGW-w64
if platform.system() == 'Windows':
    c_extension.extra_compile_args = ['-static-libgcc']
    c_extension.extra_link_args = ['-static-libgcc', '-static-libstdc++']
