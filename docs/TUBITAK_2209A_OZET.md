# TÜBİTAK 2209-A Araştırma Önerisi Özeti

**Program:** TÜBİTAK 2209-A Üniversite Öğrencileri Araştırma Projeleri Destekleme Programı (2026 Yılı 1. Dönem)  
**Proje Başlığı:** Çift Enkoderli Kablosuz Diz Goniyometresi ile Tek Kameralı İşaretleyicisiz Diz Açısı Ölçümünün Karşılaştırılması ve Gerçek Zamanlı Görselleştirme  
**Akademik Danışman:** Prof. Dr. Erkan Zergeroğlu  
**Proje Ekibi:** İbrahim Halil Doğan, Mert Canoğlu, Cem Baygın  

---

## 1. Özet ve Amaç

Bu araştırmanın temel amacı, sağ ve sol diz eklemlerinin fleksiyon-ekstansiyon hareketini eşzamanlı kaydedebilen, bataryalı ve kablosuz (Bluetooth Classic SPP) çift enkoderli bir mekanik goniyometre prototipi geliştirmek; bu düzenekten elde edilen açı verilerini, tek RGB kameradan çalışan işaretleyicisiz poz kestirimi yöntemiyle (MediaPipe Pose / BlazePose) zaman eşleştirmeli olarak karşılaştırmaktır.

Çalışma, laboratuvar tipi pahalı ve karmaşık işaretleyicili hareket yakalama sistemlerine (MoCap) bağımlılığı azaltarak, sahada ve klinik öncesi değerlendirmede kullanılabilecek düşük maliyetli, taşınabilir ve erişilebilir bir ölçüm ve doğrulama altyapısı sunmayı hedefler.

> [!NOTE]
> Bu çalışma **keşifsel teknik değerlendirme** niteliğindedir; klinik tanı veya tedavi aracı iddiası taşımamaktadır.

---

## 2. Araştırma Soruları ve Hipotezler

### Araştırma Sorusu
> Tek kameralı, işaretleyicisiz iki boyutlu poz kestirimiyle hesaplanan diz fleksiyon açısı; squat, oturup kalkma ve yürüme sırasında aynı dizden alınan enkoder ölçümlerine kıyasla ne düzeyde farklılık göstermektedir? Bu ölçüm farkları hareket türüne ve anatomik anahtar noktaların görüntüdeki görünürlüğüne göre nasıl değişmektedir?

### Hipotezler
- **H1:** Kamera düzleminin ve katılımcı konumunun sabit tutulduğu, eklem noktalarının net göründüğü kayıtlarda (squat, oturup kalkma); kamera ve enkoder açı serileri arasındaki fark (MAE / RMSE), uzuvların birbirini perdeleyebildiği düz hat yürüme kayıtlarına kıyasla anlamlı derecede daha düşük olacaktır.
- **H2:** MediaPipe görünürlük (visibility) skorlarının azalması ve geçersiz kare oranının artması, kamera tabanlı ölçümlerdeki anlık açı sapması ile pozitif yönlü (Spearman sıra korelasyonu) bir ilişki gösterecektir.

---

## 3. Donanım ve Yazılım Metodolojisi

1. **Mekanik & Donanım Katmanı:**
   - Her iki dizlik menteşesine akuple edilmiş 5000 pals/tur (PPR) çözünürlüklü artımsal enkoderler.
   - Diferansiyel hat alıcı (line receiver) devresi ile gürültü bağışıklığı ve 3.3V lojik seviye dönüşümü.
   - ESP32 PCNT (Pulse Counter) çevre birimi ile 4 kenar (4x quadrature) donanımsal sayım ($5000 \times 4 = 20.000$ sayım/tur $\approx 0.018^\circ$ açısal çözünürlük).
   - Li-ion batarya, şarj koruma devresi ve regülatör katı.

2. **Haberleşme & Paket Protokolü:**
   - Bluetooth Classic SPP üzerinden 50 Hz frekansta 28 baytlık ikili telemetri paketi iletimi.
   - Paket içeriği: Başlık (`0xAA55`), Sıra No, ESP32 Zaman Damgası (ms), Sol/Sağ Sayım, Sol/Sağ Açı, CRC16.
   - Uzaktan kontrol komutları: `Z` (Sıfırlama/Ofset), `S` (Başlat), `P` (Duraklat).

3. **Görüntü İşleme ve Poz Kestirimi:**
   - 1080p @ 30 FPS sagittal kamera kaydı (katılımcıya 2.5-3 m uzaklıkta, diz yüksekliğinde).
   - MediaPipe Pose ile kalça, diz ve ayak bileği anahtar noktalarının tespiti.
   - İki vektör arasındaki iç açı: $\theta = 180^\circ - \arccos\left(\frac{u \cdot v}{\|u\| \|v\|}\right)$.
   - Titreşim önleme için düşük geçişli hareketli ortalama / Butterworth filtresi.

4. **Senkronizasyon ve Analiz:**
   - ESP32 zaman damgaları ile bilgisayar monotonik saatinin eşleştirilmesi ve doğrusal enterpolasyonla hizalama.
   - Kayan pencere (5 sn) canlı MAE ve RMSE gösterimi.
   - Oturum sonu Bland-Altman uyum analizi (%95 Limits of Agreement: $\bar{d} \pm 1.96 \cdot SD$).

---

## 4. İş Paketleri (İP) ve Dağılımı

| İP No | İş Paketi Adı | Süre | Sorumlu(lar) | Başarı Ölçütü |
|:---:|:---|:---:|:---|:---|
| **İP 1** | Mekanik ve Sensör Altyapısı | 2 Ay | Cem Baygın, Mert Canoğlu | İki dizden tezgâhta kararlı sayım alınması (%15) |
| **İP 2** | Gömülü Yazılım ve BT Haberleşme | 2 Ay | İbrahim Halil Doğan | 50 Hz aktarım, <%1 paket kaybı, Z/S/P protokolü (%15) |
| **İP 3** | Kamera Tabanlı Açı Kestirimi | 3 Ay | Mert Canoğlu, Cem Baygın | ≥25 FPS uçtan uca işleme, açı şablon testi (%15) |
| **İP 4** | Masaüstü Arayüz ve Eşzamanlama | 3 Ay | İbrahim Halil Doğan, Cem Baygın | PyQt6 arayüzde canlı grafikler, zaman farkı <33 ms (%20) |
| **İP 5** | Tezgâh ve Yazılım Doğrulaması | 2 Ay | Tüm Ekip | 0°-120° referans açılarda tezgâh test raporu (%15) |
| **İP 6** | Katılımcı Ölçümleri ve Analiz | 3 Ay | Tüm Ekip | En az 15 tamamlanmış veri seti, MAE/RMSE/Bland-Altman raporu (%20) |

---

## 5. Risk Yönetimi ve B Planları

| Risk | Olasılık / Etki | Alınacak Tedbir (B Planı) |
|:---|:---:|:---|
| Dizlik menteşesinin anatomik eksenden kayması | Orta / Orta | Her test öncesi/sonrası sıfır kontrolü, ayarlanabilir cırt bantlar, kayma olan tekrarların dışlanarak raporlanması. |
| Enkoder sinyalinde elektromanyetik gürültü | Düşük / Yüksek | Diferansiyel sinyal alıcı devresi ve donanımsal PCNT filtresi kullanımı; tezgâhta osiloskop doğrulaması. |
| Bluetooth paket kaybı veya bağlantı kopması | Orta / Orta | Otomatik yeniden bağlanma ve sıra no denetimi; hata ayıklama oturumlarında kablolu UART yedeği. |
| MediaPipe anahtar noktalarının perdelenmesi | Yüksek / Orta | Katılımcı arka plan kontrastının artırılması; görünürlük puanı <0.6 olan karelerin geçersiz olarak filtrelenmesi. |
| Etik kurul onay sürecinin uzaması | Orta / Düşük | Başvurunun ilk haftalarda yapılması; bu süreçte donanım, tezgâh kalibrasyonu ve sentetik veri testlerinin bitirilmesi. |
