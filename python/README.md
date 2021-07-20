# snippets/python

The code snippets and odd scripts I use (and reuse) across my Python projects.

## Folder Contents

- PythonStarter contains a basic project template, featuring a setup.py and a
barebones CLI with the Click library
- scripts-portable contains 'mini-packages', small utility programs designed to
be dropped into a larger project

## Project Generation

This section of the repository loosely doubles as a dynamic new project
generator for myself, using the script setup_project.py located in the same
folder as this README. Running this script allows the user to create a new
project that uses PythonStarter as a foundation and adds desired scripts from
scripts-portable to the project as well.
