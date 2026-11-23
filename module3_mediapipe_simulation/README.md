# Modül 3: Simülasyon ve MediaPipe Kamera Tabanlı Açı Tahmini

## Genel Bakış

Bu modül, tek bir RGB kamera görüntüsünden diz fleksiyon/ekstensiyon açısının gerçek zamanlı
olarak hesaplanmasını sağlar. Sagittal düzlemde konumlandırılmış bir kamera (1080p, 30 FPS)
aracılığıyla MediaPipe Pose (BlazePose) modeli kullanılarak vücut yer işaretleri (landmark)
tespit edilir. Tespit edilen kalça, diz ve ayak bileği koordinatlarından vektörel hesaplamayla
diz açısı elde edilir. Elde edilen açı verileri, enkoder referans verileriyle zaman
senkronizasyonu yapılarak karşılaştırma analizine uygun hale getirilir.

Ayrıca, video akışı üzerine 2B şematik bacak simülasyonu çizilerek kullanıcıya anlık
görsel geri bildirim sunulur.

## MediaPipe Pipeline

Sistem aşağıdaki MediaPipe Pose (BlazePose GHUM 3D) iş akışını kullanır:

1. **Kare Yakalama**: OpenCV `VideoCapture` ile kameradan 1920×1080 çözünürlükte, 30 FPS
   kare alınır.
2. **Ön İşleme**: Her kare BGR'den RGB'ye dönüştürülür (MediaPipe giriş formatı).
3. **Poz Tahmini**: `mp.solutions.pose.Pose` modeli kareler üzerinde çalıştırılır.
4. **Landmark Çıkarımı**: 33 vücut noktasından yalnızca alt ekstremite noktaları kullanılır:
   - Kalça: `LEFT_HIP (23)` / `RIGHT_HIP (24)`
   - Diz: `LEFT_KNEE (25)` / `RIGHT_KNEE (26)`
   - Ayak Bileği: `LEFT_ANKLE (27)` / `RIGHT_ANKLE (28)`
5. **Görünürlük Kontrolü**: Her landmark'ın `visibility` skoru kontrol edilir.
   Eşik değeri 0.6'nın altındaki kareler analizden çıkarılır.

## Açı Hesaplama Matematiği

Diz açısı, kalça-diz vektörü ile diz-ayak bileği vektörü arasındaki açı olarak hesaplanır.

### Vektör Tanımları

```
V1 = (hip.x - knee.x, hip.y - knee.y)    # Kalça-Diz vektörü
V2 = (ankle.x - knee.x, ankle.y - knee.y) # Ayak Bileği-Diz vektörü
```

### Nokta Çarpım Formülü

```
cos(θ) = (V1 · V2) / (|V1| × |V2|)
θ = arccos(cos(θ))
```

Burada:
- `V1 · V2` = `V1.x × V2.x + V1.y × V2.y` (skaler çarpım)
- `|V1|` = `sqrt(V1.x² + V1.y²)` (vektör büyüklüğü)
- Sonuç radyandan dereceye çevrilir: `açı_derece = θ × (180 / π)`

### Gürültü Azaltma

Ham açı sinyaline düşük geçişli Butterworth filtresi uygulanır:
- Filtre tipi: 2. dereceden düşük geçişli (low-pass)
- Kesim frekansı: Ayarlanabilir (varsayılan ~6 Hz, insan diz hareketi bant genişliğine uygun)
- Örnekleme frekansı: 30 Hz (kamera FPS)

## Zaman Senkronizasyonu Stratejisi

Kamera (30 FPS) ve rotary enkoder (50 Hz) farklı örnekleme hızlarına sahip olduğundan,
karşılaştırma için zaman hizalaması gereklidir.

### Yöntem: Zaman Damgası Tabanlı Doğrusal İnterpolasyon

1. Her kamera karesine `time.perf_counter()` ile milisaniye hassasiyetinde zaman damgası
   atanır.
2. Enkoder verileri kendi zaman damgalarıyla (ESP32 `millis()`) kaydedilir.
3. Her iki zaman serisinin başlangıç anları bir senkronizasyon sinyaliyle hizalanır.
4. `numpy.interp()` kullanılarak kamera açı verileri, enkoder zaman noktalarına
   doğrusal olarak interpole edilir.
5. Böylece aynı zaman ekseninde iki sinyal karşılaştırılabilir hale gelir.

### Dikkat Edilecekler

- Kamera ve ESP32 saatleri arasında drift oluşabilir; uzun kayıtlarda periyodik
  senkronizasyon tetikleyicisi gerekebilir.
- Görünürlük filtresi nedeniyle atlanan karelerde interpolasyon boşlukları oluşabilir;
  bu boşluklar `NaN` olarak işaretlenir.

## Simülasyon Görüntüleme

Video akışı üzerine gerçek zamanlı olarak şu görsel öğeler çizilir:

- **İskelet Çizimi**: Kalça → Diz → Ayak Bileği arasında renkli çizgiler ve eklem
  noktalarında daireler.
- **Açı Yayı**: Diz noktası merkezli, hesaplanan açıyı gösteren bir yay çizimi.
- **Bilgi Paneli**: Kare üzerine yarı-saydam bir kutu içinde:
  - Anlık diz açısı (derece)
  - Landmark görünürlük skorları
  - Anlık FPS değeri
  - Kayıt süresi

## Bağımlılıklar

| Paket | Sürüm | Açıklama |
|-------|--------|----------|
| mediapipe | ≥ 0.10.0 | Poz tahmini modeli |
| opencv-python | ≥ 4.8.0 | Kamera yakalama ve görüntü işleme |
| numpy | ≥ 1.24.0 | Sayısal hesaplamalar ve interpolasyon |
| scipy | ≥ 1.11.0 | Butterworth filtre tasarımı |
| matplotlib | ≥ 3.7.0 | Opsiyonel: çevrimdışı grafik çizimi |

Kurulum:
```bash
pip install -r requirements.txt
```

## Kullanım

```bash
# Temel kullanım - varsayılan kamera (ID=0) ile başlat
python -m module3_mediapipe_simulation.src.main

# Belirli bir kamera ID'si ve çözünürlük ile
python -m module3_mediapipe_simulation.src.main --camera-id 1 --width 1920 --height 1080

# Kayıt modu - açı verilerini CSV dosyasına yaz
python -m module3_mediapipe_simulation.src.main --record --output session_01.csv
```

> **Not**: Kameranın sagittal düzlemde (yandan görünüm) konumlandırılması doğruluk
> açısından kritik öneme sahiptir. Frontal düzlem görüntüsü açı hesabında büyük
> hatalara yol açar.

## Yapılacaklar (TODO)

- [ ] `CameraCapture` sınıfı: kamera açma/kapama ve kare okuma mantığı
- [ ] `PoseDetector` sınıfı: MediaPipe Pose entegrasyonu ve landmark çıkarımı
- [ ] `AngleCalculator` sınıfı: vektörel açı hesabı implementasyonu
- [ ] `AngleCalculator`: Butterworth filtre implementasyonu
- [ ] `AngleCalculator`: interpolasyon fonksiyonu implementasyonu
- [ ] `SimulationRenderer` sınıfı: iskelet overlay çizimi
- [ ] `SimulationRenderer`: açı yayı çizimi
- [ ] `SimulationRenderer`: bilgi paneli çizimi
- [ ] Ana döngü (`main.py`): tüm bileşenlerin entegrasyonu
- [ ] Sağ/sol bacak seçimi parametre olarak eklenecek
- [ ] Görünürlük eşik değeri komut satırı parametresi olarak eklenecek
- [ ] Enkoder veri dosyası yükleme ve senkronizasyon testi
- [ ] Performans optimizasyonu: kare atlama stratejisi (gerekirse)
- [ ] Birim testleri: açı hesaplama ve interpolasyon fonksiyonları için

---

**Proje Ekibi**: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
**Akademik Danışman**: Prof. Dr. Erkan Zergeroglu
