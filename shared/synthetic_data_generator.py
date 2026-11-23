"""
Sentetik Veri Ureteci (Synthetic Data Generator)

Fiziksel ESP32 donanimi olmadan Modul 2 (masaustu arayuz) ve
Modul 3 (MediaPipe pipeline) gelistirmesini mumkun kilmak icin
gercekci telemetri paketleri ureten yardimci betik.

Kullanim:
    python shared/synthetic_data_generator.py --port COM_VIRTUAL --hz 50
    python shared/synthetic_data_generator.py --tcp 127.0.0.1:9000 --hz 50 --noise 0.5

Ozellikler:
    - Sinus dalga tabanlı diz acisi kalibi (squat hareketi simulasyonu)
    - Yapilandırılabilir gurultu seviyesi
    - Gercek 28 baytlik paket formati
    - Seri port veya TCP soket cikisi
"""

import argparse
import struct
import time
import math
from dataclasses import dataclass


# --- Sabitler ---
PACKET_HEADER = bytes([0xAA, 0x55])
COUNTS_PER_REV = 20000  # 5000 PPR x 4 (quadrature)
DEG_PER_COUNT = 360.0 / COUNTS_PER_REV


@dataclass
class GeneratorConfig:
    """Sentetik veri ureteci yapilandirmasi."""
    output_hz: int = 50           # Paket gonderi frekansi
    motion_freq: float = 0.5     # Hareket frekansi (Hz) - squat hizi
    min_angle: float = 0.0       # Minimum diz acisi (tam ekstansiyon)
    max_angle: float = 120.0     # Maksimum diz acisi (derin squat)
    noise_std: float = 0.3       # Gaussyen gurultu standart sapmasi (derece)
    left_right_offset: float = 2.0  # Sol-sag enkoder arasi sabit ofset (derece)


class SyntheticDataGenerator:
    """
    Gercekci diz acisi telemetri paketleri ureten sinif.

    TODO: Asagidaki metodlari gercekleyin:
    """

    def __init__(self, config: GeneratorConfig = None):
        """
        TODO:
            - Yapilandirmayi kaydet
            - Sayaclari sifirla (sequence number, timestamp)
            - Rastgele sayi ureteci baslat
        """
        self.config = config or GeneratorConfig()
        raise NotImplementedError("__init__() henuz gerceklenmedi")

    def generate_angle(self, elapsed_seconds: float) -> float:
        """
        Belirli bir zaman noktasi icin gercekci diz acisi uret.

        Args:
            elapsed_seconds: Baslangicintan bu yana gecen sure

        Returns:
            Diz acisi (derece)

        TODO:
            - Sinus dalgasi ile temel hareket kalibini olustur
            - min_angle ve max_angle arasinda olcekle
            - Gaussyen gurultu ekle
            - Acinin fiziksel sinirlar icinde kalmasini sagla (0-180)
        """
        raise NotImplementedError("generate_angle() henuz gerceklenmedi")

    def angle_to_counts(self, angle_deg: float) -> int:
        """
        Aci degerini enkoder sayimine donustur.

        TODO:
            - angle_deg / DEG_PER_COUNT ile sayima cevir
            - Tam sayiya yuvarla
        """
        raise NotImplementedError("angle_to_counts() henuz gerceklenmedi")

    def build_packet(self, seq: int, timestamp_ms: int,
                     left_count: int, right_count: int,
                     left_angle: float, right_angle: float) -> bytes:
        """
        28 baytlik ikili telemetri paketi olustur.

        TODO:
            - struct.pack ile alanlari paketle
            - CRC16 hesapla ve ekle
            - Header baytlarini bas tarafa koy
        """
        raise NotImplementedError("build_packet() henuz gerceklenmedi")

    def run_serial(self, port: str):
        """
        Seri port uzerinden paket akisi baslat.

        TODO:
            - pyserial ile belirtilen portu ac
            - Dongude: aci uret -> paket olustur -> porta yaz
            - 1/output_hz aralikla bekle
            - Ctrl+C ile durdurma destegi
        """
        raise NotImplementedError("run_serial() henuz gerceklenmedi")

    def run_tcp(self, host: str, port: int):
        """
        TCP soket uzerinden paket akisi baslat.

        TODO:
            - Soket olustur ve dinle
            - Baglanti gelince: dongude paket uret ve gonder
            - Baglanti kopmasini ele al
        """
        raise NotImplementedError("run_tcp() henuz gerceklenmedi")


def main():
    """
    Komut satiri giris noktasi.

    TODO:
        - argparse ile parametreleri al (--port, --tcp, --hz, --noise, --min-angle, --max-angle)
        - GeneratorConfig olustur
        - SyntheticDataGenerator baslar
        - Seri veya TCP modunda calistir
    """
    parser = argparse.ArgumentParser(
        description="Sentetik diz goniyometre verisi ureteci"
    )
    parser.add_argument("--port", type=str, help="Seri port adi (ornek: COM3)")
    parser.add_argument("--tcp", type=str, help="TCP adres:port (ornek: 127.0.0.1:9000)")
    parser.add_argument("--hz", type=int, default=50, help="Paket frekansi (varsayilan: 50)")
    parser.add_argument("--noise", type=float, default=0.3, help="Gurultu standart sapmasi")

    args = parser.parse_args()

    # TODO: Yapilandirmayi olustur ve ureticiy baslat
    print("Sentetik veri ureteci henuz gerceklenmedi. TODO'lari tamamlayin.")


if __name__ == "__main__":
    main()
