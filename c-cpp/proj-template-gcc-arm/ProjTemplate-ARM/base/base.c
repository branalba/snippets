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
 * Header file for the BASE layer of the application. Provides a interface with
 * which to initialize the hardware and RTOS layers.
 *
 */

/* ========================================================================== */
/* PRIVATE INCLUDES                                                           */
/* ========================================================================== */

/* system */
#include <stdarg.h>

/* user-defined */
#include "SEGGER_RTT.h"
#include "base.h"

/* ========================================================================== */
/* EXTERNAL VARIABLES                                                         */
/* ========================================================================== */

/* ========================================================================== */
/* PRIVATE VARIABLES                                                          */
/* ========================================================================== */

/* RTT up buffer */
uint8_t RTTupBuf[256];

/* peripheral struct instances */
I2C_HandleTypeDef hi2c1;
SPI_HandleTypeDef hspi1;
UART_HandleTypeDef huart1;

/* ========================================================================== */
/* PRIVATE FUNCTION PROTOTYPES                                                */
/* ========================================================================== */
static void SystemClock_Config ( void );
static void MX_GPIO_Init ( void );
static void MX_USART1_UART_Init ( void );
static void MX_I2C1_Init ( void );
static void MX_SPI1_Init ( void );

/* ========================================================================== */
/* EXTERNAL FUNCTION DEFINITIONS                                              */
/* ========================================================================== */

/*
 * @brief User-implemented print function for debugging
 *
 * @param *p_str: pointer to input string
 * @param args: generic C string formatting args
 *
 * @retval none
 */
void USER_PRINT ( const char *p_str, ... )
{
    /* initialize arguments */
    va_list args;
    va_start ( args, p_str );
    /* actual print implementation (s) */
    if ( RTT_LOGGING_ENABLED == 1 )
        SEGGER_RTT_printf ( 0, p_str, args );
    /* release args */
    va_end ( args );
}

/**
 * @brief Initializes all hardware peripherals
 * @retval none
 */
void Base_Chip_Init ( void )
{
    /* initialize RTT and configure the up buffer */
    SEGGER_RTT_Init();
    SEGGER_RTT_ConfigUpBuffer ( 0, "Terminal", &RTTupBuf[0], 4096,
                                SEGGER_RTT_MODE_NO_BLOCK_SKIP );

    /* print the welcome banner */
    USER_PRINT ( "\n ============================================ \n" );
    USER_PRINT ( "\n            ARM-GCC Project Template          \n" );
    USER_PRINT ( "\n ============================================ \n" );

    /************************************
     * Initializing system peripherals
     ***********************************/

    /* running HAL_Init */
    USER_PRINT ( "\nRunning HAL_Init()...\n" );
    HAL_Init();

    /* intializing clocks */
    USER_PRINT ( "\nInitializing clocks...\n" );
    SystemClock_Config();

    /* initializing GPIO */
    USER_PRINT ( "\nInitializing GPIO...\n" );
    MX_GPIO_Init();

    /* initializing USART1 */
    USER_PRINT ( "\nInitializing USART1...\n" );
    MX_USART1_UART_Init();

    /* initializing I2C1 */
    USER_PRINT ( "\nInitializing I2C1...\n" );
    MX_I2C1_Init();

    /* initializing SPI1 */
    USER_PRINT ( "\nInitializing SPI1...\n" );
    MX_SPI1_Init();

    /* print completion message before exiting */
    USER_PRINT ( "\nHardware initialization completed without errors.\n" );
}

/**
 * @brief  This function is executed in case of error occurrence.
 * @retval None
 */
void Error_Handler ( void )
{
    __disable_irq();
    while ( 1 )
    {
    }
}

/**
 * @brief Called when an assertion fails
 * @retval None
 */
void assert_failed ( uint8_t *file, uint32_t line ) {}

/* ========================================================================== */
/* PRIVATE FUNCTION DEFINITIONS                                               */
/* ========================================================================== */

/**
 * @brief System Clock Configuration
 * @retval None
 */
void SystemClock_Config ( void )
{
    RCC_OscInitTypeDef RCC_OscInitStruct = { 0 };
    RCC_ClkInitTypeDef RCC_ClkInitStruct = { 0 };

    /** Initializes the RCC Oscillators according to the specified parameters
     * in the RCC_OscInitTypeDef structure.
     */
    RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
    RCC_OscInitStruct.HSIState = RCC_HSI_ON;
    RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
    RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
    if ( HAL_RCC_OscConfig ( &RCC_OscInitStruct ) != HAL_OK )
    {
        Error_Handler();
    }
    /** Initializes the CPU, AHB and APB buses clocks
     */
    RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK | RCC_CLOCKTYPE_SYSCLK |
                                  RCC_CLOCKTYPE_PCLK1 | RCC_CLOCKTYPE_PCLK2;
    RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
    RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
    RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
    RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

    if ( HAL_RCC_ClockConfig ( &RCC_ClkInitStruct, FLASH_LATENCY_0 ) != HAL_OK )
    {
        Error_Handler();
    }
}

/**
 * @brief I2C1 Initialization Function
 * @param None
 * @retval None
 */
static void MX_I2C1_Init ( void )
{
    hi2c1.Instance = I2C1;
    hi2c1.Init.ClockSpeed = 100000;
    hi2c1.Init.DutyCycle = I2C_DUTYCYCLE_2;
    hi2c1.Init.OwnAddress1 = 0;
    hi2c1.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
    hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
    hi2c1.Init.OwnAddress2 = 0;
    hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
    hi2c1.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;
    if ( HAL_I2C_Init ( &hi2c1 ) != HAL_OK )
    {
        Error_Handler();
    }
}

/**
 * @brief SPI1 Initialization Function
 * @param None
 * @retval None
 */
static void MX_SPI1_Init ( void )
{
    /* SPI1 parameter configuration*/
    hspi1.Instance = SPI1;
    hspi1.Init.Mode = SPI_MODE_MASTER;
    hspi1.Init.Direction = SPI_DIRECTION_2LINES;
    hspi1.Init.DataSize = SPI_DATASIZE_8BIT;
    hspi1.Init.CLKPolarity = SPI_POLARITY_LOW;
    hspi1.Init.CLKPhase = SPI_PHASE_1EDGE;
    hspi1.Init.NSS = SPI_NSS_SOFT;
    hspi1.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_2;
    hspi1.Init.FirstBit = SPI_FIRSTBIT_MSB;
    hspi1.Init.TIMode = SPI_TIMODE_DISABLE;
    hspi1.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
    hspi1.Init.CRCPolynomial = 10;
    if ( HAL_SPI_Init ( &hspi1 ) != HAL_OK )
    {
        Error_Handler();
    }
}

/**
 * @brief USART1 Initialization Function
 * @param None
 * @retval None
 */
static void MX_USART1_UART_Init ( void )
{
    huart1.Instance = USART1;
    huart1.Init.BaudRate = 115200;
    huart1.Init.WordLength = UART_WORDLENGTH_8B;
    huart1.Init.StopBits = UART_STOPBITS_1;
    huart1.Init.Parity = UART_PARITY_NONE;
    huart1.Init.Mode = UART_MODE_TX_RX;
    huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
    huart1.Init.OverSampling = UART_OVERSAMPLING_16;
    if ( HAL_UART_Init ( &huart1 ) != HAL_OK )
    {
        Error_Handler();
    }
}

/**
 * @brief GPIO Initialization Function
 * @param None
 * @retval None
 */
static void MX_GPIO_Init ( void )
{
    GPIO_InitTypeDef GPIO_InitStruct = { 0 };

    /* GPIO Ports Clock Enable */
    __HAL_RCC_GPIOC_CLK_ENABLE();
    __HAL_RCC_GPIOA_CLK_ENABLE();
    __HAL_RCC_GPIOB_CLK_ENABLE();

    /*Configure GPIO pin Output Level */
    HAL_GPIO_WritePin ( GPIOC, GPIO_PIN_13, GPIO_PIN_RESET );

    /*Configure GPIO pin Output Level */
    HAL_GPIO_WritePin ( GPIOB,
                        GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_14 | GPIO_PIN_15,
                        GPIO_PIN_RESET );

    /*Configure GPIO pin : PC13 */
    GPIO_InitStruct.Pin = GPIO_PIN_13;
    GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    HAL_GPIO_Init ( GPIOC, &GPIO_InitStruct );

    /*Configure GPIO pins : PB0 PB1 PB14 PB15 */
    GPIO_InitStruct.Pin = GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_14 | GPIO_PIN_15;
    GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    HAL_GPIO_Init ( GPIOB, &GPIO_InitStruct );

    /*Configure GPIO pin : PB10 */
    GPIO_InitStruct.Pin = GPIO_PIN_10;
    GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init ( GPIOB, &GPIO_InitStruct );
}

/**
 * @brief  Period elapsed callback in non blocking mode
 * @note   This function is called  when TIM3 interrupt took place, inside
 * HAL_TIM_IRQHandler(). It makes a direct call to HAL_IncTick() to increment
 * a global variable "uwTick" used as application time base.
 * @param  htim : TIM handle
 * @retval None
 */
void HAL_TIM_PeriodElapsedCallback ( TIM_HandleTypeDef *htim )
{
    if ( htim->Instance == TIM3 )
    {
        HAL_IncTick();
    }
}
