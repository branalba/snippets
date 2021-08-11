#!/usr/bin/env python

###############################################################################
# class definitions
###############################################################################


class X86 ():
    EXEC_EXT = ''
    CC_PREFIX = ''
    MCU_FLAGS = ''
    C_DEFS = ''
    LDFLAGS = '-lm'
    CFLAGS = '-Wall'


class STM32F103 ():
    MCU_FLAGS = '-mcpu=cortex-m3 -mthumb'
    C_DEFS = '-DUSE_HAL_DRIVER -DSTM32F103x6'
    CFLAGS = '-Wall -fdata-sections -ffunction-sections -Og -gdwarf-2'
    LDFLAGS = '-lc -lnosys -specs=nano.specs -Wl,-Map=$build_dir/$target.map,--cref -Wl,--gc-sections'
    CC_PREFIX = 'arm-none-eabi-'
    EXEC_EXT = '.elf'

###############################################################################
# function definitions
###############################################################################


def strStich(arr):
    out = ''
    for item in arr:
        if item != '':
            out = out + ' ' + str(item)
    return out[1:]


def writeVar(var_name, var_val):
    out = var_name + ' = ' + var_val
    return out


def writeRule(rule_name, rule_cmd):
    out = '\nrule ' + rule_name + '\n' + '    command = ' + rule_cmd + '\n'
    return out


def srcToObj(path_to_src):
    src_filename = path_to_src[path_to_src.rfind('/') + 1:-2]
    return src_filename + '.o'


def writeSrcObjBuild(path_to_src):
    src_filename = path_to_src[path_to_src.rfind('/') + 1:-2]
    out = 'build $build_dir/' + src_filename + '.o: cc ' + path_to_src + '\n'
    return out


def writeAsmObjBuild(path_to_src):
    src_filename = path_to_src[path_to_src.rfind('/') + 1:-2]
    out = 'build $build_dir/' + src_filename + '.o: as ' + path_to_src + '\n'
    return out

###############################################################################
# project config
###############################################################################


OUTPUT_FILE = 'build.ninja'

# name of the project, also name output executables
PROJ_NAME = 'arm-gcc-project'

# platform, i.e., the target that the code will run on
platform = STM32F103()

# the root folder for the project, i.e., the highest-level directory that
# contains all source code
PROJ_ROOT = 'arm-gcc-project'

# the directory to generate build outputs
BUILD_DIR = 'build'

# enter sources and includes as bare paths only with respect to source root
C_SOURCES = [
    'app/main.c',
    'base/os/freertos.c',
    'app/stm32f1xx_it.c',
    'base/chip/stm32f1xx_hal_msp.c',
    'base/chip/stm32f1xx_hal_timebase_tim.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_gpio_ex.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_rcc.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_rcc_ex.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_gpio.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_dma.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_cortex.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_pwr.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_flash.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_flash_ex.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_exti.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_tim.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_tim_ex.c',
    'base/chip/system_stm32f1xx.c',
    'base/os/FreeRTOS/Source/croutine.c',
    'base/os/FreeRTOS/Source/event_groups.c',
    'base/os/FreeRTOS/Source/list.c',
    'base/os/FreeRTOS/Source/queue.c',
    'base/os/FreeRTOS/Source/stream_buffer.c',
    'base/os/FreeRTOS/Source/tasks.c',
    'base/os/FreeRTOS/Source/timers.c',
    'base/os/FreeRTOS/Source/CMSIS_RTOS_V2/cmsis_os2.c',
    'base/os/FreeRTOS/Source/portable/MemMang/heap_4.c',
    'base/os/FreeRTOS/Source/portable/GCC/ARM_CM3/port.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_uart.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_i2c.c',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_spi.c',
    'base/base.c',
    'base/debug/RTT/SEGGER_RTT.c',
    'base/debug/RTT/SEGGER_RTT_printf.c',
    'app/tasks/task_blink.c'
]

C_INCLUDES = [
    'app',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy',
    'base/chip/Drivers/STM32F1xx_HAL_Driver/Inc',
    'base/os/FreeRTOS/Source/include',
    'base/os/FreeRTOS/Source/CMSIS_RTOS_V2',
    'base/os/FreeRTOS/Source/portable/GCC/ARM_CM3',
    'base',
    'base/chip',
    'base/os',
    'base/debug/RTT',
    'app/tasks',
    'base/chip/Drivers/CMSIS/Device/ST/STM32F1xx/Include',
    'base/chip/Drivers/CMSIS/Include'
]

# asm sources generally have atypical paths and thus they are not search for
# with respect to the source root. Use relative path instead
ASM_SOURCES = [
    'support/build/startup_stm32f103x6.s'
]

# linker script
LINKSCRIPT = 'support/build/STM32F103C6Tx_FLASH.ld'

###############################################################################
# begin main application - beyond this point shouldn't be edited
###############################################################################


def main():
    # create dictionary to manage source file paths
    source_items = dict()

    # c sources
    source_items['c_sources'] = [
        PROJ_ROOT + '/' + raw for raw in C_SOURCES]

    # asm sources
    source_items['asm_sources'] = ASM_SOURCES

    # create dictionary to manage items that will become variables in build.ninja
    var_items = dict()

    # compiler and assembler commands, respecively
    var_items['cc'] = platform.CC_PREFIX + 'gcc'
    var_items['as'] = platform.CC_PREFIX + 'gcc -x assembler-with-cpp'

    # build directory and project name
    var_items['build_dir'] = BUILD_DIR
    var_items['target'] = PROJ_NAME

    # flags
    var_items['cflags'] = strStich([
        platform.CFLAGS,
        platform.C_DEFS,
        platform.MCU_FLAGS,
        '-g'
    ])

    # add a linker script if available
    if LINKSCRIPT.strip() != '':
        link_arg = '-T' + LINKSCRIPT
    else:
        link_arg = ''

    var_items['ldflags'] = strStich([
        platform.LDFLAGS,
        platform.MCU_FLAGS,
        link_arg
    ])

    # includes - also used to generate a .ccls file for language server
    incl_arr = ['-I' + PROJ_ROOT + '/' + raw for raw in C_INCLUDES]
    var_items['c_includes'] = strStich(incl_arr)
    with open('.ccls', 'w') as cclsf:
        if (platform.CC_PREFIX == 'arm-none-eabi-'):
            cclsf.write('-I/usr/arm-none-eabi/include\n')
        for path in incl_arr:
            cclsf.write(path + '\n')

    # open build file for writing
    buildfile = open(OUTPUT_FILE, 'w')

    # write variables
    buildfile.writelines([writeVar(name, val) + '\n'
                         for name, val in var_items.items()])

    # --- rule definitions
    buildfile.write(
        writeRule('cc', '$cc -c $cflags $c_includes $in -o $out'))
    buildfile.write(writeRule('as', '$as -c $cflags $c_includes $in -o $out'))
    buildfile.write(writeRule('link', '$cc $in $ldflags -o $out'))
    buildfile.write('\n')

    # --- building object files
    # build C source files
    for src in source_items['c_sources']:
        buildfile.write(writeSrcObjBuild(src))
    # build asm files
    for asm in source_items['asm_sources']:
        buildfile.write(writeAsmObjBuild(asm))
    buildfile.write('\n')

    # --- link object files to generate executable
    buildfile.write('build $build_dir/$target' + platform.EXEC_EXT + ': link ' +
                    strStich(['$build_dir/' + srcToObj(src) for src in source_items['c_sources'] + source_items['asm_sources']]))
    buildfile.write('\n')

    # we are done, close the file before exiting
    buildfile.close()


if __name__ == '__main__':
    main()
