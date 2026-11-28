# Module 1: Hardware & Encoder Signal Processing

## Overview

This module encapsulates the embedded systems layer responsible for high-precision knee joint flexion angle measurement. Running on an ESP32 microcontroller, the firmware decodes quadrature signals from two 5000 PPR incremental rotary encoders (left and right knees) using dedicated hardware Pulse Counter (PCNT) peripherals. Angle telemetry is packetized and transmitted at $50\text{ Hz}$ over Bluetooth Classic SPP to desktop and mobile hosts.

## Hardware Components

| Component | Description |
|---|---|
| **ESP32-DevKitC** | Dual-core 240 MHz microcontroller with native Bluetooth Classic support |
| **Incremental Encoders (x2)** | 5000 PPR, differential line driver output ($A, \bar{A}, B, \bar{B}$), left and right knees |
| **AM26C32 Line Receivers (x2)** | Quad differential line receiver ICs — convert differential signals to single-ended 3.3V logic |
| **Power Regulation** | Single-cell Li-ion battery with protection circuit and 3.3V/5V LDO regulators |
| **Passives** | $120\,\Omega$ termination resistors, 100 nF decoupling capacitors, pull-up resistors |

## Wiring Architecture

For detailed pin assignments and schematic tables, refer to [docs/WIRING.md](docs/WIRING.md).

```text
Encoders (Differential Output)
    A+/A-, B+/B-
        │
        ▼
AM26C32 Differential Receiver
    Single-ended 3.3V TTL output (A, B)
        │
        ▼
ESP32 GPIO Pins
    Dedicated PCNT hardware counter input channels
```

* **Left Encoder:** AM26C32 #1 $\rightarrow$ ESP32 PCNT Unit 0 (GPIO 34, GPIO 35)
* **Right Encoder:** AM26C32 #2 $\rightarrow$ ESP32 PCNT Unit 1 (GPIO 32, GPIO 33)

## Angular Resolution Calculation

With 5000 Pulses Per Revolution (PPR) and 4x quadrature edge decoding:

$$\text{Counts Per Revolution} = 5000 \times 4 = 20{,}000\text{ counts/rev}$$
$$\text{Angular Step} = \frac{360^\circ}{20{,}000} = 0.018^\circ/\text{count}$$
$$\theta(t) = \left(N(t) - N_{offset}\right) \times 0.018^\circ$$

This level of resolution provides sub-tenth degree precision, exceeding typical clinical requirements.

## Firmware Architecture

### Device State Machine

```text
IDLE  ──(CMD_START)──►  STREAMING
  ▲                        │
  │                   (CMD_PAUSE)
  │                        │
  └──────(CMD_ZERO)────────┘
          ▼
       CALIBRATING
```

* **IDLE:** Bluetooth connected, waiting for commands; telemetry halted.
* **STREAMING:** Telemetry packets transmitted at a steady 50 Hz.
* **CALIBRATING:** Zero-offset command processed; current counter values set as $N_{offset}$.

### Binary Packet Specification (28 Bytes)

| Field | Type | Size | Description |
|---|---|---|---|
| `header` | uint8[2] | 2 B | Fixed sync header: `0xAA`, `0x55` |
| `seq` | uint32 | 4 B | Incremental sequence counter |
| `timestamp_ms` | uint32 | 4 B | Milliseconds since ESP32 boot |
| `left_count` | int32 | 4 B | Left knee raw quadrature count |
| `right_count` | int32 | 4 B | Right knee raw quadrature count |
| `left_angle` | float32 | 4 B | Left knee angle in degrees |
| `right_angle` | float32 | 4 B | Right knee angle in degrees |
| `crc16` | uint16 | 2 B | CRC-16/CCITT over bytes 0-25 |

### Control Protocol (Single-Byte ASCII)

| Command | Character | Description |
|---|---|---|
| **Zero** | `'Z'` | Calibrates current position as $0.0^\circ$ baseline |
| **Start** | `'S'` | Begins periodic 50 Hz telemetry streaming |
| **Pause** | `'P'` | Halts telemetry streaming |

## Build & Flash (PlatformIO)

```bash
cd module1_hardware_encoder
pio run
pio run --target upload
pio device monitor --baud 115200
```

## TODO Checklist

- [ ] Configure PCNT Unit 0 and Unit 1 for dual quadrature decoding
- [ ] Implement hardware glitch filtering on PCNT inputs
- [ ] Implement 16-bit PCNT overflow/underflow interrupt handler for 32-bit tracking
- [ ] Initialize Bluetooth Classic SPP server with name `ESP32_GONIOMETER`
- [ ] Implement 50 Hz FreeRTOS periodic timer task
- [ ] Implement CRC-16/CCITT calculation function
- [ ] Implement ASCII command parser (`'Z'`, `'S'`, `'P'`)
