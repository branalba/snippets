# fileselectcli

A simple, light file explorer written in Python. Provides a more visual way for a
user to select a file during application runtime

## How to Use

The primary function to use is get_path(). Use any desired directory as the start
directory, the function's only argument (os.getcwd() will return the current
working directory). The file explorer will then run and allow you to select a file
or folder, at which point the explorer will exit and the function will return the
full path selected.

Example program:

```Python
import fileselectcli

# print the path to a selected folder
print ( get_path( os.getcwd() ) )
```

## TODOs

- Commenting overall
- Restrict inputs in two main ways
  - Disallow inputs of indices outside of current listdir output
  - Distinguish between files and folders in cases such as moving into a directory
- Provide a visual distinction between files and folders
- Allow selection of multiple files/folders in a single input, specifically for
selection purposes
