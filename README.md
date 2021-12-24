# branalba/snippets

My repository of template starter projects and commonly used functions and
simple applications that I use across my software projects.

## Repository Guide

The repo is organized by programming language.

### Python

- PythonStarter
  - a template I used for almost all newly created python projects,
incl. a scalable application structure and packaging options with both
setuptools and Pyinstaller. The main.py source file also features the
building blocks for a CLI interface using the Click module,  which I make
use of in almost all of my scripts and applications.
- scripts-portable: a collection of useful Python scripts I wrote and reuse across
many projects
  - fileselectcli - a lightweight, minimal file selection utility that provides
a visual, terminal-based way to select files during runtime. Inspired by the
[ranger](https://github.com/ranger/ranger) file explorer.
  - csvreader - a collection of functions used to help preview and import data
from csv files. Useful for applications that need to process a lot of different
csv files with varying columns and structure

### C/C++

- arm-gcc-project-template
  - An in-the-works template project eventually intended for configuration
and use with most microcontrollers using arm-none-eabi as a compiler. The
initial project is set up to run a blink script in a FreeRTOS task on a
blue pill STM32F103 chip.
- header/source file templates
