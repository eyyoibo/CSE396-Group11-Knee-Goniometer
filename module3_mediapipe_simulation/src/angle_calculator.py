"""
angle_calculator.py - Açı Hesaplama ve Sinyal İşleme Modülü

Bu modül, kalça-diz-ayak bileği noktalarından vektörel yöntemle diz açısı
hesaplar. Ayrıca gürültü azaltma (Butterworth filtre) ve farklı örnekleme
hızlarındaki verileri hizalama (doğrusal interpolasyon) işlevleri içerir.

Açı Hesaplama Yöntemi:
    V1 = hip - knee       (kalça-diz vektörü)
    V2 = ankle - knee     (ayak bileği-diz vektörü)
    cos(θ) = (V1 · V2) / (|V1| × |V2|)
    θ = arccos(cos(θ))    (radyan → derece)

Proje Ekibi: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
Akademik Danışman: Prof. Dr. Erkan Zergeroglu
"""

import numpy as np


class AngleCalculator:
    """Diz açısı hesaplama, filtreleme ve zaman hizalama işlemleri."""

    def compute_angle(
        self,
        hip_point: tuple[float, float],
        knee_point: tuple[float, float],
        ankle_point: tuple[float, float],
    ) -> float:
        """Üç eklem noktasından diz açısını hesapla.

        Kalça-diz ve ayak bileği-diz vektörleri arasındaki açıyı
        nokta çarpım (dot product) formülüyle hesaplar.

        Hesaplama adımları:
            1. V1 = (hip.x - knee.x, hip.y - knee.y)
            2. V2 = (ankle.x - knee.x, ankle.y - knee.y)
            3. dot = V1[0]*V2[0] + V1[1]*V2[1]
            4. mag1 = sqrt(V1[0]² + V1[1]²)
            5. mag2 = sqrt(V2[0]² + V2[1]²)
            6. cos_angle = dot / (mag1 * mag2)
            7. cos_angle değerini [-1, 1] aralığına kırp (sayısal kararlılık)
            8. angle_rad = arccos(cos_angle)
            9. angle_deg = angle_rad * 180 / π

        Args:
            hip_point: Kalça noktası (x, y) koordinatları.
            knee_point: Diz noktası (x, y) koordinatları.
            ankle_point: Ayak bileği noktası (x, y) koordinatları.

        Returns:
            Derece cinsinden diz açısı (0-180 aralığında).
        """
        # TODO: V1 ve V2 vektörlerini numpy dizisi olarak oluştur
        # TODO: np.dot ile skaler çarpımı hesapla
        # TODO: np.linalg.norm ile vektör büyüklüklerini hesapla
        # TODO: Sıfıra bölme koruması ekle (büyüklük sıfırsa 0.0 döndür)
        # TODO: np.clip ile cos değerini [-1, 1] aralığına kırp
        # TODO: np.arccos ile açıyı radyan cinsinden hesapla
        # TODO: np.degrees ile dereceye çevir ve döndür
        raise NotImplementedError("Açı hesaplama henüz uygulanmadı")

    def apply_butterworth_filter(
        self,
        signal: np.ndarray,
        cutoff_hz: float = 6.0,
        fs: float = 30.0,
        order: int = 2,
    ) -> np.ndarray:
        """Ham açı sinyaline düşük geçişli Butterworth filtresi uygula.

        İnsan diz hareketi tipik olarak 0-6 Hz bant genişliğindedir.
        Bu filtreyle yüksek frekanslı gürültü bileşenleri bastırılır.

        Filtre tasarım adımları:
            1. Nyquist frekansı: fn = fs / 2
            2. Normalize kesim frekansı: wn = cutoff_hz / fn
            3. scipy.signal.butter ile filtre katsayıları (b, a) üret
            4. scipy.signal.filtfilt ile sıfır fazlı filtreleme uygula

        Args:
            signal: Filtrelenecek açı zaman serisi (1B numpy dizisi).
            cutoff_hz: Kesim frekansı Hz cinsinden (varsayılan 6.0 Hz).
            fs: Örnekleme frekansı Hz cinsinden (varsayılan 30.0 Hz, kamera FPS).
            order: Filtre derecesi (varsayılan 2).

        Returns:
            Filtrelenmiş açı sinyali (aynı boyutta numpy dizisi).
        """
        # TODO: scipy.signal.butter kullanarak filtre katsayılarını hesapla
        #   - btype='low' (düşük geçişli)
        #   - Wn = cutoff_hz / (fs / 2) (normalize frekans)
        # TODO: scipy.signal.filtfilt ile çift yönlü (sıfır fazlı) filtreleme
        # TODO: Sinyal çok kısaysa (< 3 * order kadar örnek) filtrelemeden döndür
        raise NotImplementedError("Butterworth filtre henüz uygulanmadı")

    def interpolate_to_encoder_timestamps(
        self,
        camera_timestamps: np.ndarray,
        camera_angles: np.ndarray,
        encoder_timestamps: np.ndarray,
    ) -> np.ndarray:
        """Kamera açı verilerini enkoder zaman noktalarına interpole et.

        Kamera 30 FPS, enkoder 50 Hz örnekleme hızına sahip olduğundan,
        karşılaştırma için kamera verilerinin enkoder zaman eksenine
        hizalanması gerekir.

        Yöntem:
            numpy.interp ile doğrusal (lineer) interpolasyon uygulanır.
            Enkoder zaman aralığı dışında kalan noktalar NaN ile işaretlenir.

        Args:
            camera_timestamps: Kamera kare zaman damgaları (saniye, 1B dizi).
            camera_angles: Kamera ile hesaplanan açı değerleri (derece, 1B dizi).
            encoder_timestamps: Enkoder veri zaman damgaları (saniye, 1B dizi).

        Returns:
            Enkoder zaman noktalarına interpole edilmiş açı değerleri.
            Kamera zaman aralığı dışındaki noktalar NaN olarak döner.
        """
        # TODO: camera_timestamps ve camera_angles boyut kontrolü
        # TODO: np.interp ile doğrusal interpolasyon uygula
        # TODO: Enkoder zaman noktalarından kamera aralığı dışında kalanları
        #       NaN ile işaretle (extrapolasyon yapma)
        # TODO: Görünürlük filtresi nedeniyle atlanan karelerdeki boşlukları
        #       NaN olarak koru
        raise NotImplementedError("Interpolasyon henüz uygulanmadı")
