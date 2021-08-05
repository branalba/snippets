/**
 * @file
 * @author Brandon Alba <branalba42@gmail.com>
 *
 * @section LICENSE
 * 
 * Copyright © 2021 Brandon Alba
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the “Software”), to deal in the
 * Software without restriction, including without limitation the rights to use, copy, 
 * modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
 * and to permit persons to whom the Software is furnished to do so, subject to the 
 * following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
 * INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
 * PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
 * CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 * @section DESCRIPTION
 *
 * Header file for the BASE layer of the application. Provides a interface with which to
 * initialize the hardware and RTOS layers.
 *
 */

/* define to prevent recursive inclusion */
#ifndef __BASE_H__
#define __BASE_H__

/* Includes */
#include "stm32f1xx_hal.h"

/* defines */
#define RTT_LOGGING_ENABLED (1u)

/* Exported function prototypes */
void Base_Chip_Init(void);
void Error_Handler(void);
void USER_PRINT(const char* p_str, ...);

#endif
