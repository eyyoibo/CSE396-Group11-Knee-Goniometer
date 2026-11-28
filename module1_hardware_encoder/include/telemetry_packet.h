/**
 * @file telemetry_packet.h
 * @brief Knee Goniometer - Binary Telemetry Packet Definitions & Constants
 *
 * Defines the packed 28-byte binary telemetry frame, command codes,
 * and hardware encoder resolution conversion parameters.
 *
 * Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
 */

#ifndef TELEMETRY_PACKET_H
#define TELEMETRY_PACKET_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ===================== Hardware Constants ===================== */

#define PACKET_HEADER_0         0xAA
#define PACKET_HEADER_1         0x55

/** Encoder resolution parameters */
#define ENCODER_PPR             5000        /* Pulses Per Revolution            */
#define QUADRATURE_MULTIPLIER   4           /* 4x quadrature edge decoding      */
#define COUNTS_PER_REV          (ENCODER_PPR * QUADRATURE_MULTIPLIER)  /* 20000 */
#define DEG_PER_COUNT           (360.0f / (float)COUNTS_PER_REV)       /* 0.018 */

/** Streaming frequency */
#define TX_FREQ_HZ              50          /* 50 Hz streaming rate             */
#define TX_PERIOD_MS            (1000 / TX_FREQ_HZ)                    /* 20 ms */

/** Exact packet payload size */
#define PACKET_SIZE             28

/* ===================== Command Definitions ===================== */

/**
 * @brief Single-byte ASCII control commands received over Bluetooth SPP.
 */
typedef enum {
    CMD_ZERO    = 'Z',   /**< Calibrate current encoder counts to 0.0 degrees */
    CMD_START   = 'S',   /**< Start continuous 50 Hz telemetry streaming       */
    CMD_PAUSE   = 'P'    /**< Pause telemetry streaming                        */
} command_t;

/* ===================== Device State Definitions ===================== */

typedef enum {
    STATE_IDLE        = 0,  /**< Waiting for connection / paused                */
    STATE_STREAMING   = 1,  /**< Actively transmitting 50 Hz telemetry packets  */
    STATE_CALIBRATING = 2   /**< Processing zero-calibration command            */
} device_state_t;

/* ===================== Telemetry Packet Structure ===================== */

/**
 * @brief 28-byte packed binary telemetry frame transmitted over Bluetooth SPP.
 */
typedef struct __attribute__((packed)) {
    uint8_t  header[2];      /**< Fixed magic bytes: {0xAA, 0x55}               */
    uint32_t seq_num;        /**< Incremental packet counter                    */
    uint32_t timestamp_ms;   /**< Uptime timestamp in milliseconds              */
    int32_t  left_count;     /**< Left knee cumulative quadrature count         */
    int32_t  right_count;    /**< Right knee cumulative quadrature count        */
    float    left_angle;     /**< Left knee calculated angle (degrees)          */
    float    right_angle;    /**< Right knee calculated angle (degrees)         */
    uint16_t crc16;          /**< CRC-16/CCITT checksum over bytes 0-25         */
} telemetry_packet_t;

_Static_assert(sizeof(telemetry_packet_t) == PACKET_SIZE, "telemetry_packet_t must be exactly 28 bytes");

/* ===================== Function Prototypes ===================== */

uint16_t compute_crc16(const uint8_t *data, uint16_t length);
void build_telemetry_packet(telemetry_packet_t *pkt, uint32_t seq,
                            int32_t left_count, int32_t right_count,
                            float left_angle, float right_angle);
float counts_to_degrees(int32_t counts, int32_t offset);

#ifdef __cplusplus
}
#endif

#endif /* TELEMETRY_PACKET_H */
