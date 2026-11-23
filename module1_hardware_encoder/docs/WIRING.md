# Kablolama Şeması

> Diz Gonyometresi — Enkoder, Diferansiyel Alıcı ve ESP32 Bağlantıları

## Genel Bilgi

Enkoderlerin diferansiyel çıkışları (A+/A-, B+/B-) doğrudan ESP32'ye bağlanamaz. AM26C32 diferansiyel hat alıcı IC kullanılarak sinyaller 3.3V TTL seviyesine dönüştürülür. Her enkoder için bir adet AM26C32 kullanılır (toplam 2 adet).

## Enkoder → AM26C32 Bağlantıları

### Sol Enkoder (Enkoder 1)

| Enkoder Pini | Sinyal | AM26C32 #1 Pini | AM26C32 Fonksiyonu |
|---|---|---|---|
| A+ | Kanal A pozitif | 1A (Pin 1) | Alıcı 1 pozitif giriş |
| A- | Kanal A negatif | 1B (Pin 2) | Alıcı 1 negatif giriş |
| B+ | Kanal B pozitif | 2A (Pin 4) | Alıcı 2 pozitif giriş |
| B- | Kanal B negatif | 2B (Pin 5) | Alıcı 2 negatif giriş |
| VCC | Enkoder besleme | — | 5V regülatör çıkışı |
| GND | Toprak | — | Ortak toprak |

### Sağ Enkoder (Enkoder 2)

| Enkoder Pini | Sinyal | AM26C32 #2 Pini | AM26C32 Fonksiyonu |
|---|---|---|---|
| A+ | Kanal A pozitif | 1A (Pin 1) | Alıcı 1 pozitif giriş |
| A- | Kanal A negatif | 1B (Pin 2) | Alıcı 1 negatif giriş |
| B+ | Kanal B pozitif | 2A (Pin 4) | Alıcı 2 pozitif giriş |
| B- | Kanal B negatif | 2B (Pin 5) | Alıcı 2 negatif giriş |
| VCC | Enkoder besleme | — | 5V regülatör çıkışı |
| GND | Toprak | — | Ortak toprak |

## AM26C32 → ESP32 Bağlantıları

### AM26C32 #1 (Sol Enkoder) → ESP32

| AM26C32 #1 Pini | Fonksiyon | ESP32 GPIO | PCNT Birimi |
|---|---|---|---|
| 1Y (Pin 3) | Kanal A TTL çıkışı | GPIO 34 | PCNT 0 — SIG |
| 2Y (Pin 6) | Kanal B TTL çıkışı | GPIO 35 | PCNT 0 — CTRL |

### AM26C32 #2 (Sağ Enkoder) → ESP32

| AM26C32 #2 Pini | Fonksiyon | ESP32 GPIO | PCNT Birimi |
|---|---|---|---|
| 1Y (Pin 3) | Kanal A TTL çıkışı | GPIO 32 | PCNT 1 — SIG |
| 2Y (Pin 6) | Kanal B TTL çıkışı | GPIO 33 | PCNT 1 — CTRL |

## AM26C32 Güç ve Etkinleştirme Bağlantıları

Her iki AM26C32 IC için aynı bağlantılar uygulanır:

| AM26C32 Pini | Fonksiyon | Bağlantı |
|---|---|---|
| VCC (Pin 16) | IC besleme | 3.3V (ESP32 3V3 pini) |
| GND (Pin 8) | Toprak | Ortak GND |
| 1EN (Pin 14) | Alıcı 1 etkinleştirme | GND (aktif düşük, daima etkin) |
| 2EN (Pin 11) | Alıcı 2 etkinleştirme | GND (aktif düşük, daima etkin) |

> **Not:** Kullanılmayan alıcı girişleri (3A/3B, 4A/4B) boşta bırakılabilir. Enable pinleri (3EN, 4EN) VCC'ye bağlanarak devre dışı tutulmalıdır.

## Güç Dağıtımı

| Kaynak | Hedef | Gerilim | Açıklama |
|---|---|---|---|
| USB / LiPo batarya | AMS1117-5.0 girişi | 7-12V | Ham güç kaynağı |
| AMS1117-5.0 çıkışı | Enkoder VCC (x2) | 5V | Enkoder besleme |
| ESP32 3V3 pini | AM26C32 VCC (x2) | 3.3V | IC besleme |
| Ortak GND | Tüm bileşenler | 0V | Ortak referans |

## Dekuplaj Kapasitörleri

Her güç pinine mümkün olduğunca yakın yerleştirilmelidir:

| Konum | Kapasitör |
|---|---|
| AM26C32 #1 — VCC-GND arası | 100nF seramik |
| AM26C32 #2 — VCC-GND arası | 100nF seramik |
| AMS1117-5.0 girişi | 10µF elektrolitik |
| AMS1117-5.0 çıkışı | 10µF elektrolitik + 100nF seramik |

## Önemli Notlar

- GPIO 34 ve GPIO 35 yalnızca giriş olarak kullanılabilir (dahili pull-up yoktur). Harici pull-up gerekmez çünkü AM26C32 çıkışları aktif sürücülüdür.
- Kablo uzunluğu 2 metreyi geçerse, diferansiyel hat sonlandırma dirençleri (120Ω) eklenmelidir.
- Tüm GND bağlantıları tek bir noktada birleştirilmeli (yıldız topraklama) ve toprak döngüsünden kaçınılmalıdır.
