# IP - A Convenient Toolbox for Image Processing

IP is a package that integrates basic functions and packages for image processing used in our course.

## Installation

We assume you have set up the environment with conda.

### Installation via Git
If you have installed `git` and added `git` and `conda` to your `PATH`, you can install IP via git:

- Open a terminal or `anaconda (powershell) prompt`
- Activate your environment with `conda activate env_name` (change `env_name` to the environment you would like to install the package in)
- Run `pip install git+https://github.com/Kris311/IP_test.git` (change the URL if you make a copy of this repository)

### Installation from Local Files

Alternatively, you can install IP from local files:

- Download and extract this repository from the drop-down menu `<>Code`-`Download ZIP`
- Open a terminal or `anaconda (powershell) prompt`
- Change the directory with `cd path_to_extracted_folder`
- Activate your environment with `conda activate my_env` (change `env_name` to the environment you would like to install the package in)
- Run `pip install .`

## Testing

After the installation, you can test IP with:

```python
from IP import *
ones(10)
```

## Making Modifications to IP.py

The original IP.py is located at `IP/IP.py`. Modifications to it will not directly reflect in the installed IP package unless you reinstall it.

If you have incorporated other packages during your modification, please add them to the `setup.py` `install_requires`, so that these dependencies are automatically installed along with IP.

[Here](https://docs.python.org/3/distutils/setupscript.html) is a detailed tutorial about how to write the setup script.

[Here](https://github.com/navdeep-G/setup.py) is a good template for setup.py.
