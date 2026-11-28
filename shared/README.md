# Shared Utilities & Cross-Module Tools

This directory contains cross-cutting utilities, data schemas, and hardware-free simulation tools utilized across all modules.

---

## 1. Components

### `packet_parser.py`
High-throughput binary packet parser for unpacking and verifying the 28-byte hardware telemetry frame streamed by the ESP32.
- Scans continuous byte streams for magic header `0xAA 0x55`
- Unpacks little-endian C struct payload
- Computes and verifies CRC-16/CCITT checksum integrity
- Returns typed `TelemetryPacket` instances

### `synthetic_data_generator.py`
Hardware-in-the-loop simulator enabling development of Module 2 (Desktop GUI) and Module 3 (Temporal Alignment) without physical ESP32 or encoder hardware.
- Generates realistic cyclical knee flexion kinematics (simulated squat motion)
- Adds configurable Gaussian noise
- Transmits valid 28-byte binary packets via virtual COM ports or local TCP sockets (`127.0.0.1:9000`) at 50 Hz

### `sample_session.csv`
Canonical reference dataset demonstrating the synchronized multi-channel CSV export schema.

---

## 2. Usage Examples

```bash
# Launch synthetic 50 Hz squat generator over local TCP socket
python shared/synthetic_data_generator.py --tcp 127.0.0.1:9000 --hz 50 --noise 0.3

# Launch synthetic generator over virtual serial port
python shared/synthetic_data_generator.py --port COM_VIRTUAL --hz 50
```
