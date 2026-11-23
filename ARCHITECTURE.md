# Sistem Mimarisi

Bu belge, Diz Gonyometresi ve Poz Tahmin Karşılaştırma Sisteminin genel mimarisini açıklar.

## Sisteme Genel Bakış

Sistem, diz eklemi açısını iki bağımsız yöntemle ölçer ve bu ölçümleri karşılaştırır:

1. **Donanımsal Ölçüm:** Diz eklemine bağlanan rotary encoder'lar ile doğrudan mekanik açı ölçümü
2. **Görüntü Tabanlı Ölçüm:** Kamera görüntüsünden MediaPipe Pose ile vücut noktalarını tespit ederek açı hesaplaması

Her iki ölçüm akışı zaman damgalı olarak kaydedilir ve masaüstü arayüzde yan yana karşılaştırılır.

## Modül Yapısı

```
┌─────────────────────────────────────────────────────────────────┐
│                        SİSTEM MİMARİSİ                         │
├─────────────┬──────────────┬───────────────┬────────────────────┤
│     M1      │      M2      │      M3       │        M4          │
│  Donanım &  │  Masaüstü    │  Kamera &     │   Mobil            │
│  Gömülü     │  Arayüz      │  Görüntü      │   Uygulama         │
│  Yazılım    │  (PyQt6)     │  İşleme       │   (React Native)   │
│             │              │  (MediaPipe)  │                    │
├─────────────┴──────────────┴───────────────┴────────────────────┤
│                     SHARED (Paylaşılan Araçlar)                 │
│        Paket Ayrıştırıcı  ·  Sentetik Veri  ·  Protokoller     │
└─────────────────────────────────────────────────────────────────┘
```

## Veri Akışı

### Encoder Veri Akışı (Donanım → Yazılım)

```
┌──────────────┐     GPIO      ┌──────────┐    Bluetooth   ┌──────────────┐
│   Rotary     │  Kesmeleri    │          │    Classic     │  Masaüstü    │
│  Encoder'lar ├──────────────►│  ESP32   ├───────────────►│  GUI (M2)    │
│  (2 adet)    │               │          │    SPP         │              │
└──────────────┘               │          │                └──────────────┘
                               │          │    BLE GATT    ┌──────────────┐
                               │          ├───────────────►│  Mobil       │
                               │          │                │  Uygulama    │
                               └──────────┘                │  (M4)        │
                                                           └──────────────┘
```

**Adımlar:**
1. İki adet quadrature rotary encoder, diz ekleminin fleksiyon/ekstansiyon açısını mekanik olarak ölçer
2. ESP32 mikrodenetleyicisi GPIO kesmeleri aracılığıyla encoder sinyallerini okur
3. Ham encoder darbeleri derece cinsinden açıya dönüştürülür
4. Açı verisi, zaman damgası ve kontrol bilgileriyle birlikte 28 baytlık bir pakete dönüştürülür
5. Paket, Bluetooth Classic SPP (masaüstü) ve BLE GATT (mobil) üzerinden iletilir

### Kamera Veri Akışı (Görüntü → Açı)

```
┌──────────┐    Video     ┌──────────┐   Landmark    ┌──────────┐
│  USB /   │   Kareleri   │ MediaPipe│   Koordinat   │   Açı    │
│  Dahili  ├─────────────►│   Pose   ├──────────────►│ Hesapla- │
│  Kamera  │              │          │   Verileri    │  yıcı    │
└──────────┘              └──────────┘               └──────────┘
```

**Adımlar:**
1. USB veya dahili kamera OpenCV ile video akışı yakalar
2. Her kare MediaPipe Pose modeline gönderilir
3. Model, 33 vücut noktasını (landmark) tespit eder
4. Kalça, diz ve ayak bileği noktalarının 2B/3B koordinatları alınır
5. Bu üç noktadan vektörel açı hesaplanır (atan2 yöntemiyle)

### Veri Birleştirme ve Karşılaştırma

İki veri akışı masaüstü GUI'de (M2) buluşur:

```
┌───────────────────────┐
│  Encoder Açı Verisi   │──┐
│  (28 bayt paket)      │  │   Zaman Damgası    ┌────────────────────┐
└───────────────────────┘  ├──Eşleştirmesi──────►│  Karşılaştırma     │
┌───────────────────────┐  │                     │  Modülü             │
│  Kamera Açı Verisi    │──┘                     │  · Fark hesaplama   │
│  (MediaPipe çıktısı)  │                        │  · İstatistik       │
└───────────────────────┘                        │  · CSV kayıt        │
                                                 └────────────────────┘
```

Her iki veri kaynağı milisaniye çözünürlüğünde zaman damgası taşır. Masaüstü uygulamadaki karşılaştırma modülü, en yakın zaman damgasına göre eşleştirme yaparak iki ölçümün farkını hesaplar.

## Teknoloji Yığını

| Bileşen | Teknoloji | Dil | Açıklama |
|---------|-----------|-----|----------|
| Mikrodenetleyici | ESP32-WROOM-32 | — | Çift çekirdekli, BT/BLE destekli |
| Firmware geliştirme | ESP-IDF v5.x | C | Resmi Espressif geliştirme çatısı |
| Encoder | Quadrature Rotary Encoder | — | 360°/tur, A/B kanal çıkışlı |
| Masaüstü GUI | PyQt6 | Python 3.10+ | Çapraz platform masaüstü arayüz |
| Gerçek zamanlı grafik | pyqtgraph | Python | Yüksek performanslı veri görselleştirme |
| Bluetooth (masaüstü) | PyBluez / bleak | Python | SPP ve BLE istemci kütüphaneleri |
| Görüntü yakalama | OpenCV 4.x | Python | Kamera erişimi ve görüntü işleme |
| Poz tahmini | MediaPipe Pose | Python | Google'ın vücut noktası tespit modeli |
| Mobil uygulama | React Native | TypeScript | Çapraz platform mobil geliştirme |
| BLE (mobil) | react-native-ble-plx | TypeScript | React Native BLE kütüphanesi |

## İletişim Protokolü (28 Bayt Paket)

ESP32'den gönderilen her veri paketi sabit 28 bayt uzunluğundadır:

| Ofset | Boyut (bayt) | Alan | Açıklama |
|-------|-------------|------|----------|
| 0 | 2 | `header` | Paket başlangıç işareti (`0xAA55`) |
| 2 | 1 | `packet_id` | Sıralı paket numarası (0-255, döngüsel) |
| 3 | 1 | `status` | Cihaz durum bayrakları |
| 4 | 4 | `timestamp` | Milisaniye cinsinden zaman damgası (uint32) |
| 8 | 4 | `encoder1_raw` | Encoder 1 ham darbe sayısı (int32) |
| 12 | 4 | `encoder2_raw` | Encoder 2 ham darbe sayısı (int32) |
| 16 | 4 | `angle_deg` | Hesaplanan açı (float32, derece) |
| 20 | 4 | `angular_vel` | Açısal hız (float32, derece/saniye) |
| 24 | 2 | `crc16` | CRC-16 kontrol toplamı |
| 26 | 2 | `footer` | Paket bitiş işareti (`0x55AA`) |

### Durum Bayrakları (status alanı)

| Bit | Anlamı |
|-----|--------|
| 0 | Encoder 1 bağlı |
| 1 | Encoder 2 bağlı |
| 2 | Kalibrasyon tamamlandı |
| 3 | Düşük pil uyarısı |
| 4-7 | Ayrılmış (gelecek kullanım) |

## Paylaşılan Araçlar

`shared/` dizini, birden fazla modül tarafından kullanılan ortak bileşenleri içerir:

### Paket Ayrıştırıcı (`shared/packet_parser/`)
28 baytlık ikili paketi ayrıştırır ve yapılandırılmış veriye dönüştürür. Python (M2, M3), C (M1 test), ve JavaScript (M4) implementasyonları mevcuttur. Tüm implementasyonlar aynı ayrıştırma mantığını paylaşır.

### Sentetik Veri Üreteci (`shared/synthetic_data/`)
Donanım olmadan test yapabilmek için gerçekçi 28 baytlık paketler üretir. Yapılandırılabilir açı dizileri, gürültü ekleme ve hata senaryoları desteklenir.

### Protokol Tanımları (`shared/protocols/`)
Paket formatı sabitleri, durum bayrakları ve sürüm bilgileri. Tüm modüller bu tanımları referans alır.
