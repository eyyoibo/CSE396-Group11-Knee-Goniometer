"""
Telemetry Packet Parser Module

Decodes and validates 28-byte packed binary telemetry frames
streamed by the ESP32 firmware over Bluetooth Classic SPP.

Frame Specification:
    Header(2B) + SeqNum(4B) + Timestamp(4B) + LeftCount(4B) +
    RightCount(4B) + LeftAngle(4B) + RightAngle(4B) + CRC16(2B)
    = 28 Bytes Total

Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
"""

import struct
from dataclasses import dataclass
from typing import Optional

PACKET_HEADER = bytes([0xAA, 0x55])
PACKET_SIZE = 28
STRUCT_FORMAT = "<2sIIiiffH"


@dataclass
class TelemetryPacket:
    """Represents an unpacked and validated telemetry frame."""
    sequence_number: int
    timestamp_ms: int
    left_count: int
    right_count: int
    left_angle: float
    right_angle: float


class PacketParser:
    """
    Parser and CRC-16 validator for binary hardware telemetry packets.
    """

    def parse(self, raw_data: bytes) -> Optional[TelemetryPacket]:
        """
        Unpacks and validates a 28-byte raw telemetry slice.

        Args:
            raw_data: 28-byte raw binary slice.

        Returns:
            TelemetryPacket instance if valid, None if malformed or CRC invalid.
        """
        if len(raw_data) != PACKET_SIZE:
            return None

        if raw_data[:2] != PACKET_HEADER:
            return None

        try:
            header, seq, ts, lc, rc, la, ra, crc = struct.unpack(STRUCT_FORMAT, raw_data)
        except struct.error:
            return None

        calculated_crc = self.compute_crc16(raw_data[:26])
        if calculated_crc != crc:
            return None

        return TelemetryPacket(
            sequence_number=seq,
            timestamp_ms=ts,
            left_count=lc,
            right_count=rc,
            left_angle=la,
            right_angle=ra,
        )

    def find_packet_start(self, buffer: bytes) -> int:
        """
        Scans a byte buffer for the magic header sequence (0xAA 0x55).

        Returns:
            Start index of header if found, -1 otherwise.
        """
        return buffer.find(PACKET_HEADER)

    def compute_crc16(self, data: bytes) -> int:
        """
        Computes standard CRC-16/CCITT checksum over input bytes.
        """
        crc = 0xFFFF
        for byte in data:
            crc ^= (byte << 8)
            for _ in range(8):
                if crc & 0x8000:
                    crc = ((crc << 1) ^ 0x1021) & 0xFFFF
                else:
                    crc = (crc << 1) & 0xFFFF
        return crc

    def validate_packet(self, raw_data: bytes) -> bool:
        """Returns True if raw data satisfies packet formatting and bounds."""
        pkt = self.parse(raw_data)
        if pkt is None:
            return False
        return 0.0 <= pkt.left_angle <= 180.0 and 0.0 <= pkt.right_angle <= 180.0
