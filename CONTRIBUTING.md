# Katkıda Bulunma Rehberi

Bu belge, projeye katkıda bulunmak isteyen geliştiriciler için temel kuralları ve süreçleri açıklar.

## Nasıl Katkıda Bulunulur

1. İlgili bir **Issue** oluşturun veya mevcut bir issue'yu kendinize atayın
2. Uygun isimlendirme kuralına göre bir **dal (branch)** oluşturun
3. Değişikliklerinizi yapın ve testleri çalıştırın
4. Bir **Pull Request** açın ve gözden geçirme sürecini takip edin

## Dal İsimlendirme Kuralları

Her dal, çalışılan modülü ve yapılan işin türünü açıkça belirtmelidir.

### Format

```
<tür>/module<modül_no>/<kısa-açıklama>
```

### Türler

| Önek | Kullanım |
|------|----------|
| `feature/` | Yeni özellik geliştirme |
| `fix/` | Hata düzeltme |
| `refactor/` | Kod yeniden düzenleme |
| `test/` | Test ekleme veya güncelleme |
| `docs/` | Dokümantasyon değişikliği |

### Örnekler

```
feature/module1/encoder-interrupt-handler
fix/module2/bluetooth-reconnection
refactor/module3/angle-calculation-pipeline
test/module4/ble-connection-tests
docs/architecture-diagram-update
```

> **Not:** Birden fazla modülü ilgilendiren değişikliklerde `shared` etiketi kullanılabilir:
> `feature/shared/packet-parser-crc`

## Commit Mesajı Formatı

Her commit mesajı, ilgili modülü belirten bir önek ile başlamalıdır.

### Format

```
[M<modül_no>] <değişiklik açıklaması>
```

### Modül Önekleri

| Önek | Modül |
|------|-------|
| `[M1]` | Donanım ve Gömülü Yazılım (ESP32, encoder) |
| `[M2]` | Masaüstü Arayüz (PyQt6 GUI) |
| `[M3]` | Kamera ve Görüntü İşleme (MediaPipe) |
| `[M4]` | Mobil Uygulama (React Native) |
| `[SHARED]` | Paylaşılan araçlar ve yardımcı modüller |
| `[DOCS]` | Dokümantasyon |
| `[CI]` | Sürekli entegrasyon ve derleme yapılandırması |

### Örnekler

```
[M1] Quadrature encoder GPIO kesme yapılandırması eklendi
[M2] Gerçek zamanlı açı grafiği kaydırma hatası düzeltildi
[M3] MediaPipe landmark tespiti için birim testleri eklendi
[M4] BLE GATT servis keşfi iyileştirildi
[SHARED] Paket ayrıştırıcı CRC-16 doğrulama desteği eklendi
[DOCS] ARCHITECTURE.md veri akış diyagramı güncellendi
```

## Kod Gözden Geçirme Süreci

1. PR açıldığında en az **bir takım üyesi** gözden geçirme yapmalıdır
2. Gözden geçirici, aşağıdaki konulara dikkat eder:
   - Kodun mevcut mimariyle tutarlılığı
   - Testlerin yeterliliği ve doğruluğu
   - Modül sınırlarına uygunluk (bir modülün kodu başka bir modüle sızmamalı)
   - Stil kurallarına uyum
3. Gerekli düzeltmeler yapıldıktan sonra gözden geçirici onay verir
4. Onay alındıktan sonra PR, `main` dalına birleştirilir

## PR Öncesi Test Gereksinimleri

Pull Request açmadan önce aşağıdaki adımları tamamlayın:

### Python Modülleri (M2, M3)
```bash
# Birim testlerini çalıştırın
pytest tests/ -v

# Kod stil kontrolü yapın
flake8 src/ --max-line-length=100

# Tip kontrolü yapın
mypy src/
```

### ESP32 Firmware (M1)
```bash
# Derleme kontrolü yapın
idf.py build

# Varsa birim testlerini çalıştırın
idf.py -T test build
```

### Mobil Uygulama (M4)
```bash
# Testleri çalıştırın
npm test

# Lint kontrolü yapın
npm run lint
```

## Kod Stili Kuralları

### Genel
- Kod tanımlayıcıları (değişken, fonksiyon, sınıf adları) **İngilizce** yazılır
- Yorumlar ve kullanıcıya yönelik metinler **Türkçe** yazılabilir
- Her dosyanın başında kısa bir açıklama yorumu bulunmalıdır

### Python
- **PEP 8** standartlarına uyulur
- Tüm fonksiyonlarda **tip ipuçları (type hints)** kullanılır
- Docstring formatı: **Google style**
- Maksimum satır uzunluğu: **100 karakter**

### C (ESP-IDF)
- Fonksiyon ve değişken isimleri: `snake_case`
- Modül fonksiyonları modül adıyla öne eklenir: `encoder_read_angle()`
- Donanım register erişimleri detaylı yorumlanır

### JavaScript / TypeScript
- **Airbnb stil rehberi** takip edilir
- Fonksiyonel bileşenler ve hook'lar tercih edilir
- Mümkün olan yerlerde TypeScript kullanılır
