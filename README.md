# Diz Goniyometresi ve Kamera Tabanli Poz Kestirimi Karsilastirma Sistemi

> Cift enkoderli kablosuz diz goniyometresi ile tek kameradan isaretleyicisiz poz kestirimi (MediaPipe Pose) yontemini gercek zamanli karsilastiran ve sonuclari goruntuleyen acik kaynakli biyomekanik olcum platformu.

**TUBiTAK 2209-A Universite Ogrencileri Arastirma Projeleri Destekleme Programi**

---

## Proje Ekibi

| Rol | Isim |
|-----|------|
| Arastirmaci / Gelistirici | Ibrahim Halil Dogan |
| Arastirmaci / Gelistirici | Mert Canoglu |
| Arastirmaci / Gelistirici | Cem Baygin |
| Akademik Danisman | Prof. Dr. Erkan Zergeroglu |

---

## Arastirma Sorusu

Tek kamerali, isaretleyicisiz 2D poz kestirimiyle hesaplanan diz fleksiyon acisi; squat, oturup kalkma ve yurume gorevlerinde cift enkoderli mekanik goniyometreye kiyasla ne duzeyde sapma gostermektedir?

### Hipotezler

- **H1:** Sagittal duzlemin sabit tutuldugu gorevlerde (squat, oturup kalkma), kamera-enkoder hata degerleri (MAE/RMSE) yurume gorevine kiyasla daha dusuk olacaktir.
- **H2:** MediaPipe landmark gorunurluk skorlarindaki dusus, anlik mutlak aci hatasiyla pozitif korelasyon gosterecektir.

---

## Sistem Mimarisi - 4 Modul

```
                    MODUL 1                           MODUL 3
              Hardware & Enkoder              Simulasyon & MediaPipe
           +---------------------+          +---------------------+
           | Sol Enkoder (5000PPR)|         | RGB Kamera (30 FPS) |
           | Sag Enkoder (5000PPR)|         | OpenCV Capture      |
           | Diff. Alici Devresi  |         | MediaPipe Pose      |
           | ESP32 PCNT (4x)     |          | Vektor Aci Hesabi   |
           | BT SPP (50 Hz)      |          | Butterworth Filtre  |
           +--------+------------+          +---------+-----------+
                    |                                  |
                    | 28-byte paket                    | aci + zaman damgasi
                    |                                  |
           +--------v-----------v------------------v---+
           |            MODUL 2                        |
           |     Masaustu Arayuz & RMSE Analizi        |
           |  - PyQt6 / PyQtGraph canli grafikler      |
           |  - Kayan pencere MAE / RMSE               |
           |  - Bland-Altman uyum analizi               |
           |  - CSV veri kaydi                          |
           +-------------------------------------------+

           +-------------------------------------------+
           |            MODUL 4                        |
           |         Mobil Uygulama                    |
           |  - BT baglantisi                          |
           |  - Canli aci gostergesi                   |
           |  - Z/S/P uzaktan kontrol                  |
           |  - Saha testi destegi                     |
           +-------------------------------------------+
```

### Modul Ozeti

| Modul | Dizin | Aciklama |
|-------|-------|----------|
| **M1** | `module1_hardware_encoder/` | ESP32 donanim PCNT sayici, diferansiyel alici devresi, aci hesabi, 50 Hz Bluetooth SPP paket akisi |
| **M2** | `module2_interface_rmse/` | PyQt6 masaustu GUI, canli aci grafikleri, kayan pencere RMSE/MAE, Bland-Altman analizi, CSV kayit |
| **M3** | `module3_mediapipe_simulation/` | Kamera akisi, MediaPipe Pose tespiti, vektor aci hesabi, zaman eslestirme, 2D simulasyon |
| **M4** | `module4_mobile_app/` | Mobil BT baglantisi, canli aci gostergesi, Z/S/P kontrol, saha testi |

---

## Veri Paketi Formati (28 Bayt)

ESP32 tarafindan 50 Hz frekansla Bluetooth SPP uzerinden gonderilen ikili paket:

| Alan | Boyut | Tip | Aciklama |
|------|-------|-----|----------|
| Header | 2B | `0xAA 0x55` | Paket baslangici |
| SeqNum | 4B | uint32 | Sirali paket numarasi |
| Timestamp | 4B | uint32 | Milisaniye cinsinden ESP32 zamani |
| LeftCount | 4B | int32 | Sol enkoder birikimli sayim |
| RightCount | 4B | int32 | Sag enkoder birikimli sayim |
| LeftAngle | 4B | float | Sol enkoder acisi (derece) |
| RightAngle | 4B | float | Sag enkoder acisi (derece) |
| CRC16 | 2B | uint16 | Hata kontrol toplami |

### Kontrol Komutlari

- `Z` - Sifir kalibrasyonu (mevcut pozisyonu 0 derece olarak ayarla)
- `S` - Veri akisini baslat
- `P` - Veri akisini durdur

---

## Hizli Baslangic

```bash
# 1. Repoyu klonla
git clone https://github.com/<kullanici-adi>/knee-goniometer-pose-estimation.git
cd knee-goniometer-pose-estimation

# 2. Python ortamini kur
python -m venv venv
.\venv\Scripts\activate          # Windows
# source venv/bin/activate       # Linux/macOS
pip install -r module2_interface_rmse/requirements.txt
pip install -r module3_mediapipe_simulation/requirements.txt

# 3. Donanimsiz test (sentetik veri ile)
python shared/synthetic_data_generator.py --port COM_VIRTUAL --hz 50
```

---

## Proje Yonetimi

- **Mimari Dokumantasyon:** [ARCHITECTURE.md](ARCHITECTURE.md)
- **GitHub Projects Panosu Rehberi:** [PROJECT_BOARD.md](PROJECT_BOARD.md)
- **Katki Kurallari:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Hazir Issue Katalogu (16 adet):** [docs/issues/](docs/issues/)
- **Agent / Copilot Talimatlari:** [AGENTS.md](AGENTS.md) ve [.github/copilot-instructions.md](.github/copilot-instructions.md)

---

## Teknoloji Yigini

| Katman | Teknoloji |
|--------|-----------|
| Mikrodenetleyici | ESP32 (ESP-IDF / PlatformIO) |
| Enkoder | 5000 PPR inkremental, diferansiyel cikis |
| Kablosuz | Bluetooth Classic SPP |
| Masaustu GUI | Python 3.10+, PyQt6, PyQtGraph |
| Poz Kestirimi | MediaPipe Pose (BlazePose) |
| Goruntu Isleme | OpenCV |
| Istatistik | NumPy, SciPy, Matplotlib, Pandas |
| Mobil | React Native / Expo (veya Flutter) |
| Surum Kontrolu | Git, GitHub Projects |

---

## Dizin Yapisi

```
knee-goniometer-pose-estimation/
+-- README.md                          # Bu dosya
+-- ARCHITECTURE.md                    # Sistem mimarisi detaylari
+-- CONTRIBUTING.md                    # Katki kurallari
+-- PROJECT_BOARD.md                   # GitHub Projects panosu rehberi
+-- AGENTS.md                          # AI agent talimatlari
+-- LICENSE                            # MIT Lisansi
+-- .gitignore
+-- .github/
|   +-- ISSUE_TEMPLATE/
|   |   +-- bug_report.md
|   |   +-- feature_request.md
|   |   +-- task.md
|   +-- pull_request_template.md
|   +-- copilot-instructions.md
+-- docs/
|   +-- issues/                        # 16 adet hazir issue dosyasi
|   +-- experiment_protocol.md         # Deney protokolu
+-- module1_hardware_encoder/
|   +-- README.md
|   +-- platformio.ini
|   +-- include/
|   |   +-- telemetry_packet.h
|   +-- src/
|   |   +-- main.c
|   +-- docs/
|       +-- WIRING.md
+-- module2_interface_rmse/
|   +-- README.md
|   +-- requirements.txt
|   +-- src/
|       +-- __init__.py
|       +-- main_window.py
|       +-- bluetooth_receiver.py
|       +-- analysis_engine.py
|       +-- csv_logger.py
+-- module3_mediapipe_simulation/
|   +-- README.md
|   +-- requirements.txt
|   +-- src/
|       +-- __init__.py
|       +-- camera_capture.py
|       +-- pose_detector.py
|       +-- angle_calculator.py
|       +-- simulation_renderer.py
+-- module4_mobile_app/
|   +-- README.md
|   +-- app/
|   |   +-- .gitkeep
|   +-- docs/
|       +-- SCREENS.md
+-- shared/
|   +-- README.md
|   +-- packet_parser.py
|   +-- synthetic_data_generator.py
+-- tests/
    +-- README.md
    +-- test_packet_parser.py
    +-- test_angle_calculator.py
    +-- test_analysis_engine.py
```

---

## Lisans

Bu proje [MIT Lisansi](LICENSE) kapsaminda lisanslanmistir.
