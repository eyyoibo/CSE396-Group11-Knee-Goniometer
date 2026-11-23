# Modül 4: Mobil Uygulama

## Genel Bakış

Bu modül, diz gonyometresi sistemine eşlik eden bir mobil uygulama geliştirmeyi
hedefler. Uygulama, Bluetooth Classic SPP üzerinden ESP32 mikrodenetleyicisine
bağlanarak gerçek zamanlı açı görüntüleme, uzaktan kalibrasyon/başlatma/duraklatma
kontrolü ve seans kaydı işlevleri sunar.

Temel motivasyon, saha testlerinde dizüstü bilgisayar taşımak zorunda kalmadan
hastayla etkileşimli ölçüm yapabilmektir. Fizyoterapist veya teknisyen, bir
elinde telefon diğer elinde gonyometre ile çalışabilir.

## Özellikler

- **Gerçek Zamanlı Açı Göstergesi**: Analog kadran (gauge) görünümünde anlık diz
  açısı gösterimi.
- **Bluetooth SPP Bağlantısı**: ESP32 ile çift yönlü seri iletişim.
- **Uzaktan Kontrol Butonları**:
  - **Z (Sıfırla)**: Enkoder sıfır kalibrasyonu komutu gönderir.
  - **S (Başlat)**: Veri kaydını başlatır.
  - **P (Duraklat)**: Veri kaydını duraklatır.
- **Seans Kaydı**: Açı verilerini zaman damgasıyla birlikte yerel depolamaya kaydeder.
- **Geçmiş Grafiği**: Önceki seansların açı-zaman grafiğini görüntüler.
- **Bağlantı Durumu Göstergesi**: Bluetooth bağlantı kalitesi ve durumu hakkında
  anlık bilgi.

## Teknoloji Yığını Seçenekleri

Uygulama geliştirme çerçevesi henüz kesinleşmemiştir. İki aday değerlendirilmektedir:

### React Native (Expo)

| Avantaj | Dezavantaj |
|---------|------------|
| JavaScript/TypeScript ekosistemi | Bluetooth Classic desteği ek kütüphane gerektirir |
| Expo ile hızlı prototipleme | Yerel modül köprüleme karmaşıklığı |
| Geniş topluluk ve kaynak | Performans yoğun grafiklerde sınırlılık |

Bluetooth kütüphanesi adayı: `react-native-bluetooth-classic`

### Flutter

| Avantaj | Dezavantaj |
|---------|------------|
| Dart dili ile tek kod tabanı | Dart öğrenme eğrisi |
| Yüksek performanslı widget motoru | Bluetooth Classic paketleri görece daha az olgun |
| Zengin animasyon ve özel widget desteği | Paket boyutu React Native'e göre büyük |

Bluetooth kütüphanesi adayı: `flutter_bluetooth_serial`

> **Karar**: Her iki seçenek de proje gereksinimleri için uygundur. Prototip aşamasında
> ekibin mevcut deneyimine göre seçim yapılacaktır.

## Uygulama Ekranları

Uygulamanın planlanmış ekran yapısı aşağıdaki gibidir. Her ekranın detaylı
açıklaması `docs/SCREENS.md` dosyasında bulunmaktadır.

1. **Bağlantı Ekranı** - Bluetooth cihaz tarama ve ESP32'ye bağlanma
2. **Gösterge Paneli** - Canlı açı kadranı ve bağlantı durumu
3. **Kontrol Ekranı** - Z/S/P butonları ve seans zamanlayıcı
4. **Geçmiş Ekranı** - Kayıtlı seans listesi ve açı grafikleri
5. **Ayarlar Ekranı** - Cihaz tercihleri, birimler, dışa aktarma

## Bluetooth Entegrasyonu

### Bağlantı Protokolü

ESP32 tarafında Bluetooth Classic SPP (Serial Port Profile) kullanılır.
Mobil uygulama, ESP32'nin yayınladığı servisi tarayarak bağlantı kurar.

### Veri Akışı

```
ESP32 → Mobil Uygulama:
  Format: "A:<açı_değeri>,T:<zaman_ms>\n"
  Örnek: "A:45.7,T:123456\n"
  Hız: 50 Hz (20 ms aralıklarla)

Mobil Uygulama → ESP32:
  Komutlar: "Z\n" (sıfırla), "S\n" (başlat), "P\n" (duraklat)
```

### Bağlantı Yönetimi

- Otomatik yeniden bağlanma (3 deneme, üstel geri çekilme)
- Bağlantı zaman aşımı: 10 saniye
- Veri tamponu: Son 500 ms veri yerel olarak tamponlanır

## Derleme ve Çalıştırma

Çerçeve seçimi yapıldıktan sonra bu bölüm güncellenecektir.

### Ön Koşullar

- Node.js ≥ 18 (React Native seçilirse) veya Flutter SDK ≥ 3.0
- Android Studio veya Xcode (platform hedefine göre)
- Fiziksel Android/iOS cihaz (Bluetooth testi için emülatör yetersizdir)

### Geliştirme Ortamı Kurulumu

```bash
# React Native / Expo seçilirse:
npx create-expo-app knee-goniometer-app
cd knee-goniometer-app
npx expo install react-native-bluetooth-classic

# Flutter seçilirse:
flutter create knee_goniometer_app
cd knee_goniometer_app
flutter pub add flutter_bluetooth_serial
```

### Çalıştırma

```bash
# React Native
npx expo start

# Flutter
flutter run
```

## Yapılacaklar (TODO)

- [ ] Teknoloji çerçevesi kararı (React Native vs Flutter)
- [ ] Proje iskeleti oluşturma
- [ ] Bağlantı ekranı: Bluetooth tarama ve cihaz listesi
- [ ] Bağlantı ekranı: SPP bağlantı kurma
- [ ] Gösterge paneli: analog kadran widget'ı
- [ ] Gösterge paneli: gelen veriyi ayrıştırma ("A:xx.x,T:xxxxx")
- [ ] Kontrol ekranı: Z/S/P buton tasarımı ve komut gönderimi
- [ ] Kontrol ekranı: seans zamanlayıcı
- [ ] Geçmiş ekranı: yerel depolamadan seans listesi
- [ ] Geçmiş ekranı: açı-zaman grafik çizimi
- [ ] Ayarlar ekranı: cihaz tercihleri ve birim seçimi
- [ ] Veri dışa aktarma (CSV formatı)
- [ ] Otomatik yeniden bağlanma mekanizması
- [ ] Bildirim: bağlantı kopma uyarısı
- [ ] UI/UX iyileştirmeleri ve renk teması
- [ ] Android ve iOS üzerinde Bluetooth izin yönetimi
- [ ] Birim testleri: veri ayrıştırma fonksiyonları

---

**Proje Ekibi**: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
**Akademik Danışman**: Prof. Dr. Erkan Zergeroglu
