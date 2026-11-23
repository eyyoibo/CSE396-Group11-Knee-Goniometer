"""
Telemetri Paketi Cozumleyici (Packet Parser)

ESP32 tarafindan Bluetooth SPP uzerinden gonderilen 28 baytlik ikili
telemetri paketlerini cozer ve dogrular.

Paket Formati:
    Header(2B) + SeqNum(4B) + Timestamp(4B) + LeftCount(4B) +
    RightCount(4B) + LeftAngle(4B) + RightAngle(4B) + CRC16(2B)
    = 28 Bayt toplam

Kullanim:
    from shared.packet_parser import PacketParser

    parser = PacketParser()
    result = parser.parse(raw_bytes)
    if result is not None:
        print(f"Sol aci: {result.left_angle}, Sag aci: {result.right_angle}")
"""

import struct
from dataclasses import dataclass
from typing import Optional


# --- Sabitler ---
PACKET_HEADER = bytes([0xAA, 0x55])
PACKET_SIZE = 28
STRUCT_FORMAT = "<2sIIiiffH"  # little-endian: header(2s), seq(I), ts(I), lc(i), rc(i), la(f), ra(f), crc(H)


@dataclass
class TelemetryPacket:
    """Cozumlenmis telemetri paketini temsil eder."""
    sequence_number: int
    timestamp_ms: int
    left_count: int
    right_count: int
    left_angle: float
    right_angle: float


class PacketParser:
    """
    ESP32 telemetri paketlerini cozen sinif.

    TODO: Asagidaki metodlari gercekleyin:
    """

    def parse(self, raw_data: bytes) -> Optional[TelemetryPacket]:
        """
        28 baytlik ham veriyi cozumle ve dogrula.

        Args:
            raw_data: 28 baytlik ham paket verisi

        Returns:
            Basarili ise TelemetryPacket, hata varsa None

        TODO:
            - Paket boyutunu kontrol et (28 bayt)
            - Header baytlarini dogrula (0xAA, 0x55)
            - struct.unpack ile alanlari ayristir
            - CRC16 dogrulamasi yap
            - TelemetryPacket nesnesi olustur ve dondur
        """
        raise NotImplementedError("parse() henuz gerceklenmedi")

    def find_packet_start(self, buffer: bytes) -> int:
        """
        Bayt tamponunda bir sonraki paket basliginin konumunu bul.

        Args:
            buffer: Aranacak bayt tamponu

        Returns:
            Baslik konumu (index), bulunamazsa -1

        TODO:
            - 0xAA 0x55 siralisinı tampon icerisinde ara
            - Bulunan ilk konumu dondur
        """
        raise NotImplementedError("find_packet_start() henuz gerceklenmedi")

    def compute_crc16(self, data: bytes) -> int:
        """
        CRC-16 kontrol toplamini hesapla.

        Args:
            data: CRC hesaplanacak baytlar (CRC alani haric ilk 26 bayt)

        Returns:
            16-bit CRC degeri

        TODO:
            - CRC-16/CCITT veya CRC-16/MODBUS algoritmasini uygula
            - ESP32 firmware ile ayni algoritmayı kullan
        """
        raise NotImplementedError("compute_crc16() henuz gerceklenmedi")

    def validate_packet(self, raw_data: bytes) -> bool:
        """
        Paketin gecerliligini kontrol et.

        TODO:
            - Boyut kontrolu
            - Header kontrolu
            - CRC kontrolu
            - Aci degerlerinin makul aralikta olup olmadigini kontrol et (0-180 derece)
        """
        raise NotImplementedError("validate_packet() henuz gerceklenmedi")
