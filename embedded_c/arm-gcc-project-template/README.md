# ARM GCC PROJECT TEMPLATE

THIS PROJECT IS A WORK IN PROGRESS; NOT ALL ITEMS IN THE FOLLOWING README HAVE
BEEN 100% IMPLEMENTED. Specifically, the Makefile (s) need work.

This project is designed to be used as a template to create any
embedded C application targeting ARM chips. The project is by default
set up to upload a generic blink script based on FreeRTOS to a "blue pill"
STM32F103C8T6 development board, but can be reconfigured to use any ARM-based
processor compiled with arm-none-eabi-. To modify:

- Edit the Makefile, instructions on what to modify/how should be indicated in
    the file itself.
- Edit the base/chip and base/os directories to use your RTOS/HAL
- Implement your own modules in the lib/ directory, i.e. lib/mymodule
    which may contain a mymodule.c, mymodule.h and possibly a README.
- Implement your application under the app/ folder, starting with a simple
    main.c/.h pair but possibly expanding to a more complex structure as needed

## Dependency Diagram

```bash
+--------------------------+
|                          <---------+
|            lib           |         |
|                          |      +--+----------------------+
+-------------+------------+      |                         |
              |                   |           app           |
              |                   |                         |
+-------------v------------+      +--+----------------------+
|                          |         |
|           base           |         |
|                          <---------+
+--------------------------+
```

- /libs should be used to house subfolders containing libraries/modules
    to be used with by the app to implement functionality such as interfacing
    with sensors, etc. Modules in libs should be such that they can be dropped
    in and out without a dependency on the application (and, if possible, the
    HAL layer), i.e., it should be possible to separate version control
    on these libraries.
- /base will contain the implementation of the OS and the core firmware/
    hardware abstraction layer implemented by the user or provided by the
    chip vendor. Setup functions for various hardware peripherals, etc.
    should also be defined here.
- /app will contain the actual application files, including but not limited to
    main.c and main.h. The application entry point will be here. In more complex
    applications like an RTOS with many tasks, the folder structure within /app
    can and should become more complex.

## Building/Usage

Build the application with ```make``` or cleanbuild with ```make clean &&
make```. I tried to set up the structure in a very debugger-agnostic way,
so there's simply a debug/ directory under support/ to store any scripts or files
related to debugging. As I use a J-Link and Segger Ozone to flash and debug,
I keep my *.jdebug files in this folder, along with a script for flashing code
with a J-Link that I can call normally or, as I like to use it, call with
```make flash```.
