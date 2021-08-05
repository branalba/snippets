# --- critial folder/file paths
PROJ_ROOT_DIR := arm-gcc-project
BUILD_SUPPORT_DIR := support/build
BUILD_DIR := build

# --- building variables (affect output during compilation, etc.)
DEBUG = 1
OPT = -Og

# --- target (i.e., executable filename. Should reflect project name)
TARGET = arm-gcc-project-template

# --- compiler (program called to compile your source files)
CC_PREFIX = arm-none-eabi-
CC = $(CC_PREFIX)gcc
AS = $(CC_PREFIX)gcc -x assembler-with-cpp
CP = $(CC_PREFIX)objcopy
SZ = $(CC_PREFIX)size
HEX = $(CP) -O ihex
BIN = $(CP) -O binary -S

# --- C flags
CPU = -mcpu=cortex-m3
MCU = $(CPU) -mthumb $(FPU) $(FLOAT-ABI)
C_DEFS = \
-DUSE_HAL_DRIVER \
-DSTM32F103x6

#####################################
# source files and include paths
####################################

# --- C sources
C_SOURCES =  \
$(PROJ_ROOT_DIR)/app/main.c \
$(PROJ_ROOT_DIR)/base/os/freertos.c \
$(PROJ_ROOT_DIR)/app/stm32f1xx_it.c \
$(PROJ_ROOT_DIR)/base/chip/stm32f1xx_hal_msp.c \
$(PROJ_ROOT_DIR)/base/chip/stm32f1xx_hal_timebase_tim.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_gpio_ex.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_rcc.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_rcc_ex.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_gpio.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_dma.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_cortex.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_pwr.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_flash.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_flash_ex.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_exti.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_tim.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_tim_ex.c \
$(PROJ_ROOT_DIR)/base/chip/system_stm32f1xx.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/croutine.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/event_groups.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/list.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/queue.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/stream_buffer.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/tasks.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/timers.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/CMSIS_RTOS_V2/cmsis_os2.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/portable/MemMang/heap_4.c \
$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/portable/GCC/ARM_CM3/port.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_uart.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_i2c.c \
$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Src/stm32f1xx_hal_spi.c \
$(PROJ_ROOT_DIR)/base/base.c \
$(PROJ_ROOT_DIR)/base/debug/RTT/SEGGER_RTT.c \
$(PROJ_ROOT_DIR)/base/debug/RTT/SEGGER_RTT_printf.c \
$(PROJ_ROOT_DIR)/app/tasks/task_blink.c

# --- ASM sources
ASM_SOURCES =  \
$(BUILD_SUPPORT_DIR)/startup_stm32f103x6.s

# --- AS includes
AS_INCLUDES =  \
-I$(PROJ_ROOT_DIR)/app

# --- C includes
C_INCLUDES =  \
-I$(PROJ_ROOT_DIR)/app \
-I$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Inc/Legacy \
-I$(PROJ_ROOT_DIR)/base/chip/Drivers/STM32F1xx_HAL_Driver/Inc \
-I$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/include \
-I$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/CMSIS_RTOS_V2 \
-I$(PROJ_ROOT_DIR)/base/os/FreeRTOS/Source/portable/GCC/ARM_CM3 \
-I$(PROJ_ROOT_DIR)/base \
-I$(PROJ_ROOT_DIR)/base/chip \
-I$(PROJ_ROOT_DIR)/base/os \
-I$(PROJ_ROOT_DIR)/base/debug/RTT \
-I$(PROJ_ROOT_DIR)/app/tasks

# -I$(PROJ_ROOT_DIR)/base/chip/Drivers/CMSIS/Device/ST/STM32F1xx/Include \
# -I$(PROJ_ROOT_DIR)/base/chip/Drivers/CMSIS/Include \
# --- compile gcc flags
ASFLAGS = $(MCU) $(AS_DEFS) $(AS_INCLUDES) $(OPT) -Wall -fdata-sections -ffunction-sections

CFLAGS = $(MCU) $(C_DEFS) $(C_INCLUDES) $(OPT) -Wall -fdata-sections -ffunction-sections

ifeq ($(DEBUG), 1)
CFLAGS += -g -gdwarf-2
endif

# Generate dependency information
CFLAGS += -MMD -MP -MF"$(@:%.o=%.d)"

#######################################
# LDFLAGS
#######################################
# link script
LDSCRIPT = $(BUILD_SUPPORT_DIR)/STM32F103C6Tx_FLASH.ld

# libraries
LIBS = -lc -lm -lnosys 
LIBDIR = 
LDFLAGS = $(MCU) -specs=nano.specs -T$(LDSCRIPT) $(LIBDIR) $(LIBS) -Wl,-Map=$(BUILD_DIR)/$(TARGET).map,--cref -Wl,--gc-sections


#######################################
# build the application 
#######################################

all: $(BUILD_DIR)/$(TARGET).elf $(BUILD_DIR)/$(TARGET).hex $(BUILD_DIR)/$(TARGET).bin

# list of objects
OBJECTS = $(addprefix $(BUILD_DIR)/,$(notdir $(C_SOURCES:.c=.o)))
vpath %.c $(sort $(dir $(C_SOURCES)))
# list of ASM program objects
OBJECTS += $(addprefix $(BUILD_DIR)/,$(notdir $(ASM_SOURCES:.s=.o)))
vpath %.s $(sort $(dir $(ASM_SOURCES)))

$(BUILD_DIR)/%.o: %.c Makefile | $(BUILD_DIR) 
	$(CC) -c $(CFLAGS) -Wa,-a,-ad,-alms=$(BUILD_DIR)/$(notdir $(<:.c=.lst)) $< -o $@

$(BUILD_DIR)/%.o: %.s Makefile | $(BUILD_DIR)
	$(AS) -c $(CFLAGS) $< -o $@

$(BUILD_DIR)/$(TARGET).elf: $(OBJECTS) Makefile
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@
	$(SZ) $@

$(BUILD_DIR)/%.hex: $(BUILD_DIR)/%.elf | $(BUILD_DIR)
	$(HEX) $< $@
	
$(BUILD_DIR)/%.bin: $(BUILD_DIR)/%.elf | $(BUILD_DIR)
	$(BIN) $< $@	
	
$(BUILD_DIR):
	mkdir $@		

#######################################
# clean up
#######################################
clean:
	-rm -fR $(BUILD_DIR)
  
#######################################
# dependencies
#######################################
-include $(wildcard $(BUILD_DIR)/*.d)

