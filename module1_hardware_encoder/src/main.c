/**
 * @file main.c
 * @brief Dual-Encoder Knee Goniometer - Firmware Core Source
 *
 * Implements hardware PCNT quadrature decoding for two 5000 PPR encoders,
 * angular conversion, packet framing, and Bluetooth Classic SPP streaming.
 *
 * Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
 */

#include <stdio.h>
#include <string.h>
#include <stdint.h>

/* ESP-IDF system headers */
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/timers.h"
#include "esp_log.h"
#include "esp_system.h"

/* PCNT (Pulse Counter) driver */
#include "driver/pulse_cnt.h"

/* Bluetooth Classic headers */
#include "esp_bt.h"
#include "esp_bt_main.h"
#include "esp_gap_bt_api.h"
#include "esp_spp_api.h"

/* Local project headers */
#include "telemetry_packet.h"

static const char *TAG = "GONIOMETER_FW";

/* Global State */
static device_state_t g_device_state = STATE_IDLE;
static uint32_t g_seq_num = 0;
static int32_t g_left_offset = 0;
static int32_t g_right_offset = 0;

/* ----------------------------------------------------------------
 * pcnt_init_encoders
 * ----------------------------------------------------------------
 * Configures ESP32 hardware PCNT units for left and right encoders.
 *
 * TODO:
 * - Configure PCNT Unit 0 for Left Encoder (GPIO 34 = A, GPIO 35 = B)
 * - Configure PCNT Unit 1 for Right Encoder (GPIO 32 = A, GPIO 33 = B)
 * - Set 4x quadrature edge decoding mode (rising/falling edges on both channels)
 * - Configure hardware glitch filter (filter threshold ~1 microsecond)
 * - Register overflow/underflow interrupt handlers for 32-bit tracking
 * - Initialize and enable both counter units
 * ---------------------------------------------------------------- */
static void pcnt_init_encoders(void)
{
    ESP_LOGI(TAG, "Initializing PCNT hardware counters for dual encoders...");
    /* TODO: Implement pulse counter hardware driver setup */
}

/* ----------------------------------------------------------------
 * calculate_angle_from_counts
 * ----------------------------------------------------------------
 * Converts raw quadrature pulse counts to joint flexion angle.
 *
 * TODO:
 * - Subtract zero-extension offset: net_counts = counts - offset
 * - Multiply by DEG_PER_COUNT (360.0 / 20000.0 = 0.018 degrees)
 * - Return calibrated angle in degrees (0.0 to 180.0 range)
 * ---------------------------------------------------------------- */
static float calculate_angle_from_counts(int32_t counts, int32_t offset)
{
    /* TODO: Implement angular conversion logic */
    return (float)(counts - offset) * (float)DEG_PER_COUNT;
}

/* ----------------------------------------------------------------
 * compute_crc16
 * ----------------------------------------------------------------
 * Calculates CRC-16/CCITT checksum over binary packet bytes.
 *
 * TODO:
 * - Polynomial: 0x1021, Initial value: 0xFFFF
 * - Compute over bytes 0 to 25 of the telemetry packet
 * ---------------------------------------------------------------- */
uint16_t compute_crc16(const uint8_t *data, uint16_t length)
{
    /* TODO: Implement standard CRC-16/CCITT algorithm */
    return 0;
}

/* ----------------------------------------------------------------
 * build_packet
 * ----------------------------------------------------------------
 * Populates fixed 28-byte binary telemetry frame.
 * ---------------------------------------------------------------- */
static void build_packet(telemetry_packet_t *pkt, uint32_t seq,
                         int32_t left_count, int32_t right_count,
                         float left_angle, float right_angle)
{
    pkt->header[0] = PACKET_HEADER_0;
    pkt->header[1] = PACKET_HEADER_1;
    pkt->seq_num = seq;
    pkt->timestamp_ms = (uint32_t)(esp_timer_get_time() / 1000);
    pkt->left_count = left_count;
    pkt->right_count = right_count;
    pkt->left_angle = left_angle;
    pkt->right_angle = right_angle;
    pkt->crc16 = compute_crc16((const uint8_t *)pkt, PACKET_SIZE - 2);
}

/* ----------------------------------------------------------------
 * bluetooth_spp_init
 * ----------------------------------------------------------------
 * Initializes Bluetooth Classic subsystem and registers SPP profile.
 *
 * TODO:
 * - Initialize NVS partition and Bluetooth controller
 * - Enable Bluedroid stack and initialize GAP/SPP profile
 * - Set device visibility and discoverable name: "ESP32_GONIOMETER"
 * ---------------------------------------------------------------- */
static void bluetooth_spp_init(void)
{
    ESP_LOGI(TAG, "Initializing Bluetooth Classic SPP...");
    /* TODO: Initialize Bluetooth stack */
}

/* ----------------------------------------------------------------
 * handle_command
 * ----------------------------------------------------------------
 * Processes single-byte ASCII commands from host ('Z', 'S', 'P').
 * ---------------------------------------------------------------- */
static void handle_command(uint8_t cmd)
{
    switch (cmd) {
        case CMD_ZERO:
            ESP_LOGI(TAG, "Command [Z]: Calibrating current positions as zero offset");
            /* TODO: Sample current PCNT counts into g_left_offset & g_right_offset */
            break;
        case CMD_START:
            ESP_LOGI(TAG, "Command [S]: Starting 50 Hz telemetry stream");
            g_device_state = STATE_STREAMING;
            break;
        case CMD_PAUSE:
            ESP_LOGI(TAG, "Command [P]: Pausing telemetry stream");
            g_device_state = STATE_IDLE;
            break;
        default:
            ESP_LOGW(TAG, "Unrecognized command received: 0x%02X ('%c')", cmd, cmd);
            break;
    }
}

/* ----------------------------------------------------------------
 * app_main
 * ----------------------------------------------------------------
 * Application entry point.
 * ---------------------------------------------------------------- */
void app_main(void)
{
    ESP_LOGI(TAG, "Starting Knee Goniometer Firmware (Group 11)...");

    pcnt_init_encoders();
    bluetooth_spp_init();

    ESP_LOGI(TAG, "Firmware initialized. Waiting for Bluetooth host connection...");

    /* Main loop stub */
    while (1) {
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
