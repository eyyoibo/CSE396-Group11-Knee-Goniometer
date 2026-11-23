# Modül 1: Donanım ve Enkoder Sinyal İşleme

## Genel Bakış

Bu modül, diz eklemi fleksiyon açısının yüksek çözünürlüklü ölçümünü gerçekleştiren gömülü sistem katmanını kapsar. ESP32 mikrodenetleyici üzerinde çalışan firmware, iki adet 5000 PPR artımlı enkoderin (sol ve sağ diz) kuadratür sinyallerini donanımsal PCNT (Pulse Counter) birimi ile çözerek açı bilgisine dönüştürür. Elde edilen veriler Bluetooth Classic SPP protokolü üzerinden 50 Hz hızla masaüstü uygulamasına iletilir.

## Donanım Bileşenleri

| Bileşen | Açıklama |
|---|---|
| **ESP32-DevKitC** | Çift çekirdekli mikrodenetleyici, dahili Bluetooth Classic desteği |
| **Artımlı Enkoder (x2)** | 5000 PPR, diferansiyel çıkışlı (A+/A-, B+/B-), sol ve sağ diz için |
| **AM26C32 (x2)** | Diferansiyel hat alıcı IC — enkoder diferansiyel sinyallerini 3.3V TTL seviyesine dönüştürür |
| **Güç Regülatörü** | Enkoder beslemesi için 5V regülatör (AMS1117-5.0 veya eşdeğeri) |
| **Pasif Bileşenler** | 100nF dekuplaj kapasitörleri, pull-up dirençleri |

## Kablolama Şeması

Detaylı kablolama tablosu için [docs/WIRING.md](docs/WIRING.md) dosyasına bakınız.

**Genel bağlantı akışı:**

```
Enkoder (Diferansiyel Çıkış)
    A+/A-, B+/B-
        │
        ▼
AM26C32 Diferansiyel Alıcı
    Tek uçlu 3.3V TTL çıkış (A, B)
        │
        ▼
ESP32 GPIO Pinleri
    PCNT birimlerine bağlı giriş pinleri
```

- Sol enkoder → AM26C32 #1 → ESP32 PCNT Birim 0 (GPIO 34, GPIO 35)
- Sağ enkoder → AM26C32 #2 → ESP32 PCNT Birim 1 (GPIO 32, GPIO 33)

## Açı Hesaplama

Her enkoder 5000 PPR çözünürlüğe sahiptir. 4x kuadratür çözme ile:

```
Devir başına darbe = 5000 × 4 = 20.000 sayım/devir
Açısal çözünürlük  = 360° / 20.000 = 0,018°/sayım
Açı (derece)       = sayım_değeri × 0,018
```

Bu çözünürlük, klinik gonyometre ölçümlerinin çok altında bir hassasiyet sağlar.

## Firmware Mimarisi

### Durum Makinesi

Cihaz aşağıdaki durumlarda çalışır:

```
IDLE  ──(CMD_START)──►  STREAMING
  ▲                        │
  │                   (CMD_PAUSE)
  │                        │
  └──────(CMD_ZERO)────────┘
          ▼
       CALIBRATING
```

- **IDLE:** Bağlantı bekleniyor veya duraklatılmış, veri gönderilmiyor.
- **STREAMING:** 50 Hz frekansta telemetri paketleri gönderiliyor.
- **CALIBRATING:** Sıfırlama komutu alındı, sayaçlar resetleniyor.

### İkili Paket Formatı (28 Bayt)

| Alan | Tip | Boyut | Açıklama |
|---|---|---|---|
| `header` | uint8[2] | 2 B | Sabit: `0xAA`, `0x55` |
| `seq` | uint32 | 4 B | Artan sıra numarası |
| `timestamp_ms` | uint32 | 4 B | ESP32 başlangıcından itibaren milisaniye |
| `left_count` | int32 | 4 B | Sol enkoder ham sayım değeri |
| `right_count` | int32 | 4 B | Sağ enkoder ham sayım değeri |
| `left_angle` | float32 | 4 B | Sol diz açısı (derece) |
| `right_angle` | float32 | 4 B | Sağ diz açısı (derece) |
| `crc16` | uint16 | 2 B | CRC-16/CCITT kontrol toplamı |

### Komut Protokolü

Masaüstü uygulamasından gelen tek baytlık ASCII komutları:

| Komut | Karakter | İşlev |
|---|---|---|
| Sıfırla | `Z` | Her iki enkoder sayacını sıfırlar (kalibrasyon) |
| Başlat | `S` | Telemetri akışını başlatır |
| Duraklat | `P` | Telemetri akışını duraklatır |

## Derleme ve Yükleme (PlatformIO)

### Gereksinimler

- [PlatformIO Core](https://platformio.org/) veya VS Code PlatformIO eklentisi
- ESP32-DevKitC kartı
- USB kablosu

### Adımlar

```bash
# Proje dizinine geçin
cd module1_hardware_encoder

# Derleme
pio run

# Karta yükleme
pio run --target upload

# Seri monitör
pio device monitor --baud 115200
```

## Test

### Birim Testi

- Enkoderleri elle çevirerek PCNT sayım doğruluğunu seri monitörden kontrol edin.
- Tam bir tur (360°) sonrası sayacın ±20.000 değerine ulaştığını doğrulayın.
- CRC hesaplamasını bilinen veri ile karşılaştırın.

### Entegrasyon Testi

- Bluetooth SPP bağlantısını telefondan veya bilgisayardan kurun.
- `S` komutu göndererek paket akışını başlatın.
- Paket boyutunun 28 bayt olduğunu doğrulayın.
- `Z` komutu ile açı değerlerinin sıfırlandığını gözlemleyin.
- `P` komutu ile akışın durduğunu kontrol edin.

## Yapılacaklar (TODO)

- [ ] PCNT birimlerini sol ve sağ enkoder için yapılandır
- [ ] 4x kuadratür çözme modunu etkinleştir
- [ ] Açı hesaplama fonksiyonunu yaz
- [ ] Bluetooth SPP başlatma ve bağlantı yönetimi
- [ ] 28 baytlık paket oluşturma
- [ ] CRC-16 hesaplama
- [ ] Komut alma ve durum makinesi geçişleri
- [ ] 50 Hz zamanlayıcı ile periyodik gönderim
- [ ] Taşma yönetimi (PCNT 16-bit sınırı)
- [ ] Hata durumu LED göstergesi
- [ ] Derin uyku / güç tasarrufu modu
- [ ] OTA firmware güncelleme desteği
