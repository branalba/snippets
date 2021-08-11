#!/usr/bin/env python

import os

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
    LDFLAGS = '-lc'
    CC_PREFIX = 'arm-none-eabi-'
    EXEC_EXT = '.elf'

###############################################################################
# function definitions
###############################################################################


def strStich(arr):
    out = ''
    for item in arr:
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


platform = STM32F103()

config_items = dict()

config_items['root'] = 'arm-gcc-project'
# TODO: automate config_items['root']prefix
config_items['c_sources'] = [
    config_items['root'] + '/app/main.c',
    config_items['root'] + '/base/os/freertos.c',
    config_items['root'] + '/app/stm32f1xx_it.c',
    config_items['root'] + '/base/chip/stm32f1xx_hal_msp.c',
    config_items['root'] + '/base/chip/stm32f1xx_hal_timebase_tim.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_gpio_ex.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_rcc.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_rcc_ex.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_gpio.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_dma.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_cortex.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_pwr.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_flash.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_flash_ex.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_exti.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_tim.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_tim_ex.c',
    config_items['root'] + '/base/chip/system_stm32f1xx.c',
    config_items['root'] + '/base/os/FreeRTOS/Source/croutine.c',
    config_items['root'] + '/base/os/FreeRTOS/Source/event_groups.c',
    config_items['root'] + '/base/os/FreeRTOS/Source/list.c',
    config_items['root'] + '/base/os/FreeRTOS/Source/queue.c',
    config_items['root'] + '/base/os/FreeRTOS/Source/stream_buffer.c',
    config_items['root'] + '/base/os/FreeRTOS/Source/tasks.c',
    config_items['root'] + '/base/os/FreeRTOS/Source/timers.c',
    config_items['root'] +
    '/base/os/FreeRTOS/Source/CMSIS_RTOS_V2/cmsis_os2.c',
    config_items['root'] +
    '/base/os/FreeRTOS/Source/portable/MemMang/heap_4.c',
    config_items['root'] +
    '/base/os/FreeRTOS/Source/portable/GCC/ARM_CM3/port.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_uart.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_i2c.c',
    config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_spi.c',
    config_items['root'] + '/base/base.c',
    config_items['root'] + '/base/debug/RTT/SEGGER_RTT.c',
    config_items['root'] + '/base/debug/RTT/SEGGER_RTT_printf.c',
    config_items['root'] + '/app/tasks/task_blink.c'
]
config_items['asm_sources'] = [
    'support/build/startup_stm32f103x6.s'
]

var_items = dict()

var_items['build_dir'] = 'build'
var_items['target'] = 'arm-gcc-project'
var_items['cflags'] = strStich([
    platform.CFLAGS,
    platform.C_DEFS,
    platform.MCU_FLAGS,
    '-g'
])
var_items['as'] = platform.CC_PREFIX + 'gcc -x assembler-with-cpp'
var_items['cc'] = platform.CC_PREFIX + 'gcc'
# TODO: prefix of -I and config_items['root']should be automated
var_items['c_includes'] = strStich([
    '-I' + config_items['root'] + '/app',
    '-I' + config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy',
    '-I' + config_items['root'] +
    '/base/chip/Drivers/STM32F1xx_HAL_Driver/Inc',
    '-I' + config_items['root'] + '/base/os/FreeRTOS/Source/include',
    '-I' + config_items['root'] + '/base/os/FreeRTOS/Source/CMSIS_RTOS_V2',
    '-I' + config_items['root'] +
    '/base/os/FreeRTOS/Source/portable/GCC/ARM_CM3',
    '-I' + config_items['root'] + '/base',
    '-I' + config_items['root'] + '/base/chip',
    '-I' + config_items['root'] + '/base/os',
    '-I' + config_items['root'] + '/base/debug/RTT',
    '-I' + config_items['root'] + '/app/tasks',
    '-I' + config_items['root'] +
    '/base/chip/Drivers/CMSIS/Device/ST/STM32F1xx/Include',
    '-I' + config_items['root'] + '/base/chip/Drivers/CMSIS/Include'
])
var_items['ldflags'] = strStich([
    platform.MCU_FLAGS,
    '-specs=nano.specs',
    '-T' + './support/build/STM32F103C6Tx_FLASH.ld',
    '-lc',
    '-lm',
    '-lnosys',
    '-Wl,-Map=' + var_items['build_dir'] + '/' +
    var_items['target'] + '.map,--cref -Wl,--gc-sections'

])


def main():
    # open build file for writing
    buildfile = open('build.ninja', 'w')

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
    for src in config_items['c_sources']:
        buildfile.write(writeSrcObjBuild(src))
    # build asm files
    for asm in config_items['asm_sources']:
        buildfile.write(writeAsmObjBuild(asm))
    buildfile.write('\n')

    # --- link object files to generate executable
    buildfile.write('build $build_dir/$target' + platform.EXEC_EXT + ': link ' +
                    strStich(['$build_dir/' + srcToObj(src) for src in config_items['c_sources'] + config_items['asm_sources']]))
    buildfile.write('\n')

    # we are done, close the file before exiting
    buildfile.close()


if __name__ == '__main__':
    main()
