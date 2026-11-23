"""
Diz Gonyometresi — CSV Veri Kayıt Modülü

Oturum bazlı CSV dosya oluşturma, satır yazma ve
dosya kapatma işlemlerini yönetir.

Proje Ekibi: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
Danışman: Prof. Dr. Erkan Zergeroglu
"""

import csv
from pathlib import Path
from typing import Optional


class CSVLogger:
    """
    Telemetri verilerini zaman damgalı CSV dosyasına kaydeden sınıf.

    Her kayıt oturumu için benzersiz dosya adıyla yeni bir CSV dosyası
    oluşturulur. Dosya başlığı otomatik yazılır.

    CSV sütunları:
        timestamp_ms, seq, left_count, right_count,
        left_angle, right_angle, camera_angle, rmse, mae
    """

    # CSV başlık satırı
    FIELDNAMES = [
        "timestamp_ms",
        "seq",
        "left_count",
        "right_count",
        "left_angle",
        "right_angle",
        "camera_angle",
        "rmse",
        "mae",
    ]

    def __init__(self, output_dir: str = "recordings"):
        """
        @param output_dir: Kayıt dosyalarının oluşturulacağı dizin yolu
        """
        self._output_dir = Path(output_dir)
        self._file = None
        self._writer: Optional[csv.DictWriter] = None
        self._row_count = 0

    # ----------------------------------------------------------------
    # start_session
    # ----------------------------------------------------------------
    def start_session(self, session_name: Optional[str] = None) -> Path:
        """
        Yeni bir kayıt oturumu başlatır ve CSV dosyasını oluşturur.

        @param session_name: İsteğe bağlı oturum adı. Verilmezse
                             zaman damgasından otomatik oluşturulur.
        @return: Oluşturulan CSV dosyasının yolu

        TODO:
        - Çıktı dizinini oluştur (yoksa)
        - Dosya adını belirle: session_name veya "session_YYYYMMDD_HHMMSS.csv"
        - Dosyayı yazma modunda aç
        - csv.DictWriter oluştur ve başlık satırını yaz
        - self._row_count sıfırla
        - Dosya yolunu döndür
        """
        return Path()

    # ----------------------------------------------------------------
    # log_row
    # ----------------------------------------------------------------
    def log_row(self, data: dict) -> None:
        """
        Bir satır veriyi CSV dosyasına yazar.

        @param data: FIELDNAMES anahtarlarını içeren sözlük

        TODO:
        - Oturum aktif değilse (self._writer None) uyarı logla ve dön
        - self._writer.writerow(data) ile satırı yaz
        - self._row_count artır
        """
        pass

    # ----------------------------------------------------------------
    # end_session
    # ----------------------------------------------------------------
    def end_session(self) -> int:
        """
        Aktif kayıt oturumunu kapatır.

        @return: Toplam yazılan satır sayısı

        TODO:
        - Dosyayı kapat (self._file.close)
        - self._writer = None yap
        - Toplam satır sayısını döndür
        """
        count = self._row_count
        self._row_count = 0
        return count

    @property
    def is_active(self) -> bool:
        """Oturum aktif mi kontrolü."""
        return self._writer is not None

    @property
    def row_count(self) -> int:
        """Mevcut oturumda yazılan satır sayısı."""
        return self._row_count
