# Uygulama Ekran Tasarımları

Bu belge, diz gonyometresi mobil uygulamasının planlanmış ekranlarını, her ekranın
amacını, temel arayüz öğelerini ve veri akışlarını açıklar.

---

## 1. Bağlantı Ekranı

### Amaç

Kullanıcının yakındaki Bluetooth cihazlarını taraması ve ESP32 gonyometre
modülüne bağlanmasını sağlar. Uygulama ilk açıldığında bu ekran gösterilir.

### Temel Arayüz Öğeleri

- **Tara Butonu**: Bluetooth taramasını başlatır/durdurur. Tarama sırasında
  dönen bir animasyon gösterilir.
- **Cihaz Listesi**: Bulunan Bluetooth cihazlarının adı ve MAC adresi ile
  listelendiği kaydırılabilir alan. Daha önce bağlanılmış cihazlar listenin
  üstünde ve farklı renkte gösterilir.
- **Bağlantı Durumu Çubuğu**: Ekranın üst kısmında bağlantı durumunu gösteren
  renkli bir bant (kırmızı: bağlı değil, sarı: bağlanıyor, yeşil: bağlı).
- **Bluetooth İzin Uyarısı**: Bluetooth veya konum izni verilmemişse
  görüntülenen bilgilendirme kartı ve ayarlara yönlendirme butonu.

### Veri Akışı

```
Kullanıcı "Tara"ya basar
  → Bluetooth adaptörü tarama başlatır
  → Bulunan cihazlar listeye eklenir
  → Kullanıcı bir cihaz seçer
  → SPP bağlantısı kurulmaya çalışılır
  → Başarılı → Gösterge Paneline otomatik geçiş
  → Başarısız → Hata mesajı ve yeniden deneme seçeneği
```

---

## 2. Gösterge Paneli (Dashboard)

### Amaç

ESP32'den gelen anlık diz açısı verisini büyük ve okunaklı bir kadran
üzerinde gösterir. Fizyoterapistin hastaya bakarken ekrana hızlıca göz
atabilmesi için tasarlanmıştır.

### Temel Arayüz Öğeleri

- **Analog Kadran (Gauge)**: Ekranın merkezi ve en büyük öğesi. 0°-180°
  aralığında derecelendirilmiş dairesel bir gösterge. İbre, anlık açı
  değerine göre hareket eder. Renk bölgeleri:
  - 0°-30°: Kırmızı (aşırı fleksiyon)
  - 30°-150°: Yeşil (normal hareket aralığı)
  - 150°-180°: Mavi (tam ekstensiyon)
- **Sayısal Açı Değeri**: Kadranın merkezinde büyük punto ile anlık açı
  (ör. "87.3°").
- **Bağlantı Durum Simgesi**: Sağ üst köşede Bluetooth bağlantı gücü
  ve durumunu gösteren küçük ikon.
- **Veri Alım Göstergesi**: Veri paketleri gelirken yanıp sönen küçük bir
  LED benzeri nokta. Veri gelmezse sabit kırmızı.
- **Min/Max Göstergesi**: Mevcut seansta kaydedilen minimum ve maksimum
  açı değerleri.

### Veri Akışı

```
Bluetooth SPP üzerinden veri alınır
  → "A:<değer>,T:<zaman>" formatı ayrıştırılır
  → Açı değeri kadran ibresi ve sayısal göstergeye yansıtılır
  → Min/max değerler güncellenir
  → Veri alım göstergesi yanıp söner
  → 500 ms veri gelmezse bağlantı uyarısı gösterilir
```

---

## 3. Kontrol Ekranı

### Amaç

ESP32'ye uzaktan kalibrasyon, kayıt başlatma ve duraklatma komutları
gönderilmesini sağlar. Aktif seans süresini takip eder.

### Temel Arayüz Öğeleri

- **Z Butonu (Sıfırla)**: Büyük, sarı renkli dairesel buton. Basıldığında
  ESP32'ye "Z\n" komutu gönderir. Enkoderin mevcut pozisyonunu sıfır
  olarak kalibre eder. Yanlışlıkla basmayı önlemek için basılı tutma
  (1 saniye) gerektirir.
- **S Butonu (Başlat)**: Büyük, yeşil renkli dairesel buton. "S\n" komutu
  gönderir. Veri kaydını başlatır. Basıldığında seans zamanlayıcı çalışmaya
  başlar.
- **P Butonu (Duraklat)**: Büyük, kırmızı renkli dairesel buton. "P\n"
  komutu gönderir. Veri kaydını duraklatır. Zamanlayıcı durur.
- **Seans Zamanlayıcısı**: Kayıt başladığından bu yana geçen süreyi
  "SS:DD:SN" formatında gösteren sayaç.
- **Durum Metni**: Mevcut durumu belirten etiket ("Boşta", "Kayıt Yapılıyor",
  "Duraklatıldı").

### Veri Akışı

```
Kullanıcı bir butona basar
  → İlgili komut dizesi ("Z\n", "S\n", "P\n") Bluetooth üzerinden gönderilir
  → ESP32 komutu alır ve uygular
  → ESP32 onay mesajı döndürür (opsiyonel)
  → Uygulama durumu güncellenir (zamanlayıcı başla/dur)
  → Kayıt modundaysa gelen açı verileri yerel depolamaya yazılır
```

---

## 4. Geçmiş Ekranı

### Amaç

Daha önce kaydedilmiş ölçüm seanslarının listesini ve her seansın açı-zaman
grafiğini görüntüler. Tedavi sürecindeki ilerlemenin takibine olanak tanır.

### Temel Arayüz Öğeleri

- **Seans Listesi**: Tarih ve saat, süre, ortalama açı bilgileriyle
  kartlar halinde listelenen geçmiş seanslar. En yeni seans üstte.
- **Seans Detay Kartı**: Bir seansa dokunulduğunda açılan genişletilmiş
  görünüm:
  - Açı-zaman çizgi grafiği (x ekseni: süre, y ekseni: açı)
  - İstatistik özeti: ortalama, min, max, standart sapma
  - ROM (Range of Motion) değeri: max - min farkı
- **Dışa Aktar Butonu**: Seçili seansın verilerini CSV dosyası olarak
  paylaşma/kaydetme seçeneği.
- **Sil Butonu**: Seçili seansı silme (onay diyalogu ile).
- **Filtre/Sıralama**: Tarihe veya süreye göre sıralama seçenekleri.

### Veri Akışı

```
Ekran açılır
  → Yerel depolamadan (SQLite veya dosya sistemi) seans listesi yüklenir
  → Kartlar halinde listelenir
  → Kullanıcı bir seansa dokunur
  → İlgili seansın tüm veri noktaları yüklenir
  → Açı-zaman grafiği çizilir ve istatistikler hesaplanır
  → "Dışa Aktar" → CSV oluştur → Paylaşma menüsü aç
```

---

## 5. Ayarlar Ekranı

### Amaç

Uygulama genelindeki tercihlerin yapılandırılmasını sağlar. Bluetooth cihaz
yönetimi, ölçüm birimi seçimi ve veri dışa aktarma seçenekleri bu ekrandan
kontrol edilir.

### Temel Arayüz Öğeleri

- **Bluetooth Cihaz Tercihleri**:
  - Varsayılan cihaz seçimi (daha önce bağlanılmış cihazlar listesi)
  - Otomatik bağlanma açma/kapama anahtarı
  - Bağlantı zaman aşımı süresi ayarı (5-30 saniye kaydırıcı)
- **Ölçüm Birimi**:
  - Açı birimi: Derece (°) veya Radyan (rad) seçim düğmesi
  - (Gelecekte: Gonyometre referans düzlemi seçimi)
- **Veri Yönetimi**:
  - Tüm seansları dışa aktar (toplu CSV)
  - Tüm verileri sil (onay diyalogu ile)
  - Depolama kullanım bilgisi (kayıt sayısı, toplam boyut)
- **Görüntüleme Tercihleri**:
  - Kadran renk teması (standart / yüksek kontrast / karanlık)
  - Ekran sönme engelleme açma/kapama
- **Hakkında**:
  - Uygulama sürüm numarası
  - Proje bilgisi ve iletişim

### Veri Akışı

```
Ekran açılır
  → Mevcut tercihler yerel depolamadan (SharedPreferences / AsyncStorage) okunur
  → Arayüz öğeleri mevcut değerlerle doldurulur
  → Kullanıcı bir değer değiştirir
  → Yeni değer anında yerel depolamaya yazılır
  → İlgili uygulama davranışı güncellenir
    (ör. birim değişikliği → kadran skalası yeniden çizilir)
```

---

**Proje Ekibi**: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
**Akademik Danışman**: Prof. Dr. Erkan Zergeroglu
