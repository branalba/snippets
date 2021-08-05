# Python Starter Project

This Python starter project is intended to be used for small to mid-sized
projects with an emphasis on portability and flexibility. It is packaged with
setuptools for easy usage during development (which also enables packaging with
pip to some local installation), and also includes a Pyinstaller script for
generating a standalone binary (or .exe on a Linux machine). It's highly recommended
to check out the [setuptools](https://setuptools.readthedocs.io/en/latest/userguide/index.html)
and [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/) docs to get an
understanding for how everything fits together.

## File Structure

```bash
PythonStarter
├── pythonstarter
│   ├── main.py
│   ├── main.spec
├── README.md
└── setup.py
```

## Installation

To install, copy an instance of the project folder (snippets/PythonStarter) to
wherever you want to store your project. Then you will want to swap out the
"PythonStarter" title for your own in a few key locations:

- The project root folder (PythonStarter -> MyProjectName)
- The application package directory (pythonstarter -> myprojectname)
- Anywhere the name occurs in setup.py
  - IMPORTANT: except for the name argument to setup() in setup.py, ensure
    your replacements to pythonstarter match exactly matches the name of the
    application package directory you set above.

Now we'll want to create a virtual environment for development. From a terminal
in the root directory of the project, ```virtualenv myenv``` to create a virtual
environment, then enter it with ```source myenv/bin/activate``` on UNIX-like systems,
or ```.\myenv\Scripts\activate.ps1``` on Windows. All following steps, including
 those related to bulding the project for release, assume that you are in a
virtual environment unless stated otherwise.

To create a pip executable for development usage, run ```pip install -e .```.
This command has three key parts: the ```install``` command will, of course, install
a program like pip would normally do for some other Python module. This will make
your program available as a command-line program as long as you are in your virtual
environment (simply run ```myprojectname``` from the terminal). The ```-e``` flag
is simply an abbreviation for ```--editable```, this means that edits to your package
myprojectname will not require a reinstall (try it by editing the click.echo() call
in the example main.py provided and rerunning the command!). Finally, the ```.```
is just telling the pip command to look in the current directory for the program
to install, which is how setup.py is called upon to work its magic.

## Development

Your main application should be written in the main() function in main.py. Setuptools
is using that function as an entry point to our program, which is why we don't need
to add a call to main() like we would if we were running the script normally with
```python main.py```. As your program grows and you want to include more scripts,
add them in the same directory as main.py and include them in main.py with
```from . import myscript1, myscript2```, where myscript1 and myscript2 are standins
for your own implementation.

One last item that came pre-added into this starter project is the inclusion of the
Click library to provide a command-line interface to the project. This lets you add
parameters to be passed into your program at runtime (such as
```myprojectname --verbose 2``` to run your program with more detailed output for
debugging) I almost always use this library in my projects in some way or another,
and it's elegant enough that if you don't use it you barely notice the commands that
are included.

## Create an Executable

When you are happy with your program, you may want to convert it to a Python-independent
executable that can be deployed on any target device for general use. This is accomplished
using Pyinstaller and the accompanying main.spec script, which contains a special
Pyinstaller Recipe from their GitHub page that is designed to package projects make
with setuptools. Simply run ```pyinstaller --onefile path/to/main.spec``` from the
directory you want the executable to be generated in. Your executable will be under
build/dist when the process is completed. Note that Pyinstaller is not a cross-compiler
and that you will generally have to run the command on Windows to get a Windows-compatible
executable, Linux for Linux, etc. You can try using tools like WSL on Windows
and Wine on Linux to "cross-compile" if needed.
