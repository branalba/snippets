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
 * Source file for the application blink task.
 *
 */

/* private includes */
#include "task_blink.h"

/* ========================================================================== */
/* PRIVATE FUNCTION PROTOTYPES                                                */
/* ========================================================================== */
void App_Task_Blink ( void *argument );

/* ========================================================================== */
/* FUNCTION DEFINITIONS                                                       */
/* ========================================================================== */

/*
 * @brief Intializes and creates the blink task
 *
 * @retval 1 if successful, 0 otherwise
 */
int App_Task_Blink_Init ( void )
{

    osThreadId_t blinkTaskHandle;
    const osThreadAttr_t blinkTask_attributes = {
        .name = "blinkTask",
        .stack_size = 128 * 4,
        .priority = (osPriority_t)osPriorityLow,
    };

    blinkTaskHandle =
        osThreadNew ( App_Task_Blink, NULL, &blinkTask_attributes );

    return ( osThreadGetState ( blinkTaskHandle ) == osThreadError ) ? 0 : 1;
}

void App_Task_Blink ( void *argument )
{
    /* infinite loop */
    while ( 1 )
    {
        osDelay ( 500 );
        HAL_GPIO_TogglePin ( GPIOC, GPIO_PIN_13 );
    }
}
