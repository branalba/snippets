/**
 * @file
 * @author Brandon Alba <branalba42@gmail.com>
 *
 * @section LICENSE
 *
 * Copyright © 2021 Brandon Alba
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the “Software”), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 * @section DESCRIPTION
 *
 * Source file for the APP layer of the application.
 *
 */

/* ========================================================================== */
/* PRIVATE INCLUDES                                                           */
/* ========================================================================== */

/* user-defined */
#include "main.h"
#include "task_blink.h"

/* ========================================================================== */
/* EXTERNAL VARIABLES                                                         */
/* ========================================================================== */

/* peripheral structs provided by HAL API */
extern I2C_HandleTypeDef hi2c1;
extern SPI_HandleTypeDef hspi1;
extern UART_HandleTypeDef huart1;

/* ========================================================================== */
/* PRIVATE VARIABLES                                                          */
/* ========================================================================== */

uint8_t uart_rx_buffer[1];
int count = 0;

/* ========================================================================== */
/* PRIVATE FUNCTION PROTOTYPES                                                */
/* ========================================================================== */
static void App_RTOS_Init ( void );

/* ========================================================================== */
/* EXTERNAL FUNCTION DEFINITIONS                                              */
/* ========================================================================== */

/* ========================================================================== */
/* PRIVATE FUNCTION DEFINITIONS                                               */
/* ========================================================================== */

/**
 * @brief  The application entry point.
 * @retval int
 */
int main ( void )
{
    /* Initialize the hardware */
    Base_Chip_Init();

    /* initialize the RTOS */
    App_RTOS_Init();

    /* infinite loop */
    while ( 1 )
    {
        /* we should never get here since the scheduler should have taken over.
         * Critical error if we reach this point */
        Error_Handler();
    }
}

/**
 * @brief Initializes the RTOS scheduler and other compoenents (tasks,
 * semaphores, etc.), then starts the kernel.
 * @retval None
 */
void App_RTOS_Init ( void )
{
    /* initialize RTOS scheduler */
    osKernelInitialize();

    /* creating the tasks */
    App_Task_Blink_Init();

    /* start the RTOS */
    osKernelStart();
}
