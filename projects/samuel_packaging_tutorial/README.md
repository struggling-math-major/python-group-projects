# Packaging Tutorial

This directory contains an example Python project created following the tutorial located at https://packaging.python.org/en/latest/tutorials/packaging-projects/.

The tutorial is a part of the official *Python Packaging User Guide* located at https://packaging.python.org/en/latest/. All information containined in this document cis paraphrased or quoted directly from that site.

Overall, the *Python Documentation* located at https://docs.python.org/3/index.html provides an in-depth single-source of truth for all things Python

This information is included for educational purposes only and should be verified before using in critical applications. See the official Python documentation for up to date information.

## Python Modules

A **module** is a basic organizational unit of Python code, i.e., a single Python file with a .py extension. Modules can be imported into other modules with the "import" statement.

## Python Packages

People commonly use the work "package" to refer to two separate but related concepts: distribution packages and import packages.

**Distribution packages** are pieces of software that you can install, e.g., the Pillow package, downloaded with the command "python3 -m pip install --upgrade Pillow". (See https://python-pillow.org.)

**Import packages** are special groupings of Python modules that can contain submodules which are imported in Python modules, e.g., once Pillow is downloaded, you import it with the command "import PIL". You can also import the Image submodule of Pillow with the command "from PIL import Image".

Import packages often contain \_\_init\_\_.py files which identify the contents of a directory as a regular package. Without an \_\_init\_\_.py file, the interpreter views the contents as a namespace package. See the Python documentation for the difference between the two.

## Python Projects

A **Python project** is a library, framework, script, plugin, application, or collection of data or other resources, or some combination thereof that is intended to be packaged into a distribution (see Python Packages section for a definition of a distribution package). You can also practically think of a Python project as anything that contains a **pyproject.toml** file.

## pyproject.toml File