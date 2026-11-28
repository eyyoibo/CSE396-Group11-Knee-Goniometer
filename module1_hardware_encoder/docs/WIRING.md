# Hardware Wiring Guide

> Dual-Encoder Knee Goniometer — Rotary Encoders, Differential Receivers & ESP32 Pinout

## 1. Overview

The incremental optical/magnetic encoders output high-speed differential RS-422 pairs ($A, \bar{A}, B, \bar{B}$) which cannot be directly connected to the ESP32 GPIOs. An AM26C32 quad differential line receiver IC converts these complementary signals to single-ended 3.3V TTL/CMOS logic levels for the ESP32 hardware Pulse Counter (PCNT) peripherals.

---

## 2. Encoder $\rightarrow$ AM26C32 Pinout

### Left Knee Encoder (Encoder 1)

| Encoder Lead | Signal | AM26C32 #1 Pin | Receiver Function |
|---|---|---|---|
| **A+** | Channel A (+) | Pin 1 (1A) | Receiver 1 Non-Inverting Input |
| **A-** | Channel A (-) | Pin 2 (1B) | Receiver 1 Inverting Input |
| **B+** | Channel B (+) | Pin 4 (2A) | Receiver 2 Non-Inverting Input |
| **B-** | Channel B (-) | Pin 5 (2B) | Receiver 2 Inverting Input |
| **VCC** | Encoder Supply | — | +5V Regulated Rail |
| **GND** | System Ground | — | Common Ground Rail |

### Right Knee Encoder (Encoder 2)

| Encoder Lead | Signal | AM26C32 #2 Pin | Receiver Function |
|---|---|---|---|
| **A+** | Channel A (+) | Pin 1 (1A) | Receiver 1 Non-Inverting Input |
| **A-** | Channel A (-) | Pin 2 (1B) | Receiver 1 Inverting Input |
| **B+** | Channel B (+) | Pin 4 (2A) | Receiver 2 Non-Inverting Input |
| **B-** | Channel B (-) | Pin 5 (2B) | Receiver 2 Inverting Input |
| **VCC** | Encoder Supply | — | +5V Regulated Rail |
| **GND** | System Ground | — | Common Ground Rail |

---

## 3. AM26C32 $\rightarrow$ ESP32 GPIO Connections

### AM26C32 #1 (Left Knee) $\rightarrow$ ESP32

| AM26C32 #1 Pin | Signal | ESP32 GPIO | PCNT Peripheral Channel |
|---|---|---|---|
| **Pin 3 (1Y)** | Channel A TTL | GPIO 34 | PCNT Unit 0 — Pulse / SIG |
| **Pin 6 (2Y)** | Channel B TTL | GPIO 35 | PCNT Unit 0 — Direction / CTRL |

### AM26C32 #2 (Right Knee) $\rightarrow$ ESP32

| AM26C32 #2 Pin | Signal | ESP32 GPIO | PCNT Peripheral Channel |
|---|---|---|---|
| **Pin 3 (1Y)** | Channel A TTL | GPIO 32 | PCNT Unit 1 — Pulse / SIG |
| **Pin 6 (2Y)** | Channel B TTL | GPIO 33 | PCNT Unit 1 — Direction / CTRL |

---

## 4. Power & Enable Configuration

Both AM26C32 ICs are configured identically:

| AM26C32 Pin | Function | Connection |
|---|---|---|
| **Pin 16 (VCC)** | Supply Voltage | +3.3V (from ESP32 3V3 pin) |
| **Pin 8 (GND)** | Ground | Common Ground |
| **Pin 14 (1EN)**| Enable 1 | GND (Active-low, permanently enabled) |
| **Pin 11 (2EN)**| Enable 2 | GND (Active-low, permanently enabled) |

> **Note:** Unused receiver channels (3A/3B, 4A/4B) should have their enable pins disabled to reduce power consumption.

---

## 5. Decoupling & Signal Integrity

* Place 100 nF ceramic capacitors directly between VCC and GND pins of each AM26C32.
* Use $120\,\Omega$ parallel termination resistors between $A$ and $\bar{A}$, as well as $B$ and $\bar{B}$ if cables exceed 1.5 meters.
* Employ star grounding to avoid ground loops between the battery, ESP32, and encoder shields.
