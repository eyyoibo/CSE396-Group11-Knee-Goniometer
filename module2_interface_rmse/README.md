# Modül 2: Masaüstü Arayüz ve RMSE Analizi

## Genel Bakış

Bu modül, enkoder tabanlı diz gonyometresinden gelen verileri gerçek zamanlı olarak alan, görselleştiren ve istatistiksel analiz yapan PyQt6 masaüstü uygulamasını kapsar. Uygulama aynı zamanda kamera tabanlı poz tahmin sistemiyle elde edilen açı değerlerini de alarak iki yöntem arasındaki uyumu Bland-Altman analizi ile değerlendirir.

## Özellikler

- **Bluetooth SPP Bağlantısı:** Seri port üzerinden cihaza bağlanma, komut gönderme (Z/S/P) ve telemetri paketlerini alma
- **Gerçek Zamanlı Grafik:** PyQtGraph ile canlı açı-zaman grafikleri; enkoder ve kamera açılarının üst üste bindirilmiş gösterimi
- **Kayan Pencere İstatistikleri:** 5 saniyelik kayan pencere üzerinden anlık MAE ve RMSE hesaplama
- **Bland-Altman Analizi:** İki ölçüm yöntemi arasındaki sistematik fark ve uyum sınırlarının görselleştirilmesi
- **CSV Veri Kaydı:** Zaman damgalı ham ve hesaplanmış verilerin CSV dosyasına kaydedilmesi
- **Oturum Yönetimi:** Kayıt başlatma/durdurma, oturum bazlı dosya oluşturma

## Mimari

```
┌─────────────────────────────────────────┐
│              MainWindow                 │
│  ┌──────────┐  ┌──────────────────┐     │
│  │ Kontrol   │  │ PyQtGraph        │     │
│  │ Paneli    │  │ Canlı Grafikler  │     │
│  └──────────┘  └──────────────────┘     │
│       │              ▲                  │
│       ▼              │                  │
│  ┌──────────────────────────────────┐   │
│  │      BluetoothReceiver (QThread) │   │
│  │      Paket okuma ve ayrıştırma   │   │
│  └──────────────────────────────────┘   │
│       │                                 │
│       ▼                                 │
│  ┌────────────────┐  ┌──────────────┐   │
│  │ AnalysisEngine │  │  CSVLogger   │   │
│  │ RMSE, MAE,     │  │  Veri kaydı  │   │
│  │ Bland-Altman   │  │              │   │
│  └────────────────┘  └──────────────┘   │
└─────────────────────────────────────────┘
```

### Bileşenler

| Dosya | Sorumluluk |
|---|---|
| `src/main_window.py` | Ana pencere, arayüz düzeni, sinyal/slot bağlantıları |
| `src/bluetooth_receiver.py` | Arka plan iş parçacığında Bluetooth seri veri okuma ve paket ayrıştırma |
| `src/analysis_engine.py` | Kayan pencere RMSE/MAE hesaplama, Bland-Altman istatistikleri |
| `src/csv_logger.py` | Oturum bazlı CSV dosya yönetimi |

## Bağımlılıklar

Tüm bağımlılıklar `requirements.txt` dosyasında listelenmiştir:

| Paket | Kullanım Amacı |
|---|---|
| PyQt6 | Masaüstü arayüz çatısı |
| pyqtgraph | Yüksek performanslı gerçek zamanlı grafikler |
| pyserial | Bluetooth seri port iletişimi |
| numpy | Sayısal hesaplamalar |
| scipy | İstatistiksel analiz fonksiyonları |
| matplotlib | Bland-Altman grafiği ve dışa aktarım görselleri |
| pandas | Veri çerçevesi işlemleri ve CSV okuma/yazma |

## Kurulum

```bash
# Sanal ortam oluşturun
python -m venv venv

# Sanal ortamı etkinleştirin (Windows)
venv\Scripts\activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

## Kullanım

```bash
# Uygulamayı başlatın
python -m src.main_window
```

1. **Bağlan:** Arayüzden Bluetooth COM portunu seçin ve "Bağlan" düğmesine tıklayın.
2. **Kalibrasyon:** "Sıfırla" düğmesi ile enkoder sayaçlarını sıfırlayın.
3. **Kayıt Başlat:** "Kayıt Başlat" düğmesine tıklayarak veri akışını ve CSV kaydını başlatın.
4. **İzleme:** Canlı grafiklerden açı değişimini ve kayan pencere istatistiklerini takip edin.
5. **Kayıt Durdur:** "Kayıt Durdur" ile oturumu sonlandırın. CSV dosyası otomatik kapatılır.
6. **Analiz:** Bland-Altman grafiğini oluşturmak için "Analiz" düğmesini kullanın.

## Analiz Yöntemleri

### MAE (Ortalama Mutlak Hata)

İki ölçüm serisi arasındaki mutlak farkların ortalamasını verir. Hata büyüklüğünün sezgisel bir ölçüsüdür.

```
MAE = (1/n) × Σ|enkoder_i − kamera_i|
```

### RMSE (Kök Ortalama Kare Hata)

Farkların karelerinin ortalamasının kareköküdür. Büyük hatalara MAE'den daha fazla ağırlık verir.

```
RMSE = √[(1/n) × Σ(enkoder_i − kamera_i)²]
```

### Bland-Altman Analizi

İki ölçüm yöntemi arasındaki uyumu değerlendirmek için kullanılan istatistiksel yöntemdir:

- **X ekseni:** İki yöntemin ortalaması → `(enkoder + kamera) / 2`
- **Y ekseni:** İki yöntem arasındaki fark → `enkoder − kamera`
- **Ortalama fark (bias):** Sistematik hatanın göstergesi
- **Uyum sınırları:** `ortalama fark ± 1.96 × standart sapma` — ölçümlerin %95'inin düşmesi beklenen aralık

Uyum sınırları klinik olarak kabul edilebilir bir aralıkta ise iki yöntem birbirinin yerine kullanılabilir.

## Yapılacaklar (TODO)

- [ ] MainWindow arayüz düzenini tasarla (kontrol paneli + grafik alanı)
- [ ] Bluetooth seri port bağlantı/kesme mantığı
- [ ] 28 baytlık ikili paket ayrıştırma ve CRC doğrulama
- [ ] PyQtGraph ile çift katmanlı canlı açı grafiği
- [ ] 5 saniyelik kayan pencere RMSE/MAE hesaplama
- [ ] Bland-Altman grafiği oluşturma ve dışa aktarma
- [ ] CSV kaydı — oturum başlatma/durdurma
- [ ] Komut gönderme düğmeleri (Z, S, P)
- [ ] Port otomatik algılama
- [ ] Hata durumu bildirimleri (bağlantı kopması, CRC hatası)
- [ ] Kamera açı verisinin entegrasyonu (Modül 3 ile arayüz)
- [ ] Karanlık tema desteği
