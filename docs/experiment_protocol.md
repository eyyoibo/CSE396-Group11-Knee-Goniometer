# Deneysel Test ve Katılımcı Ölçüm Protokolü

**Proje Ekibi:** İbrahim Halil Doğan, Mert Canoğlu, Cem Baygın  
**Akademik Danışman:** Prof. Dr. Erkan Zergeroğlu  
**TÜBİTAK 2209-A / CSE 396 Bitirme Projesi**

---

## 1. Etik Kurallar ve Gönüllü Bilgilendirmesi

1. **Etik Onay:** Tüm katılımcı testleri, yetkili üniversite etik kurulunun onay/muafiyet belgesi alındıktan sonra başlatılacaktır.
2. **Gönüllü Katılım ve Onam:** Katılımcılara çalışmanın amacı, süresi, yapılacak hareketler ve kamera kaydı detayları yazılı olarak açıklanacak ve **Bilgilendirilmiş Gönüllü Onam Formu** imzalatılacaktır.
3. **Veri Gizliliği (KVKK):**
   - Her katılımcıya rastgele bir kod verilecektir (ör. `SUBJ_01`, `SUBJ_02`).
   - Kamera kadrajı yalnızca bel altı bölgeyi (alt ekstremite) kapsayacak şekilde ayarlanacak, katılımcının yüzü kaydedilmeyecektir.
   - Ham video ve ölçüm verileri çevrimdışı yerel sürücülerde şifreli saklanacak; üçüncü taraf bulut servislerine yüklenmeyecektir.
4. **Çekilme Hakkı:** Katılımcı herhangi bir anda hiçbir gerekçe göstermeksizin ölçümü durdurma veya çalışmadan çekilme hakkına sahiptir.

---

## 2. Katılımcı Kriterleri ve Örneklem

- **Hedef Katılımcı Sayısı:** En az 15 tamamlanmış ve kalite kontrolden geçmiş veri seti (olası veri kaybına karşı 18 katılımcı davet edilecektir).
- **Dahil Edilme Kriterleri:**
  - 18 yaş ve üzeri sağlıklı yetişkinler.
  - Günlük fiziksel hareketleri (yürüme, çömelme) bağımsız ve ağrısız gerçekleştirebilen bireyler.
- **Dışlanma Kriterleri:**
  - Son 6 ay içerisinde geçirilmiş diz/ayak bileği cerrahisi veya aktif alt ekstremite ortopedik sakatlığı bulunanlar.
  - Test sırasında baş dönmesi, ağrı veya yorgunluk bildirenler.

---

## 3. Kamera ve Deney Düzeneği Kurulumu

```
               [Sabit RGB Kamera (1080p, 30 FPS)]
                              |
                              | 2.5 - 3.0 metre mesafe
                              v
   +-----------------------------------------------------+
   |           Sagittal Düzlem Hareket Alanı             |
   |                                                     |
   |  Katılımcı (Belde ESP32 kutusu + Sağ/Sol Dizlik)    |
   |                                                     |
   +-----------------------------------------------------+
```

- **Kamera Konumu:** Tripod üzerinde, zemin seviyesinden yaklaşık diz hizasında (~50 cm yükseklik), sagittal düzleme dik (90°).
- **Mesafe:** Katılımcının hareket alanına 2.5 - 3.0 metre mesafede sabit.
- **Aydınlatma:** Gölgeleri ve parlamayı azaltmak için homojen yapay iç mekan aydınlatması.
- **Kıyafet:** Eklem noktalarının rahat tespiti için kontrast renkte, diz bölgesini örtmeyen dar şort.

---

## 4. Deney Protokolü ve Hareket Görevleri

Her katılımcı iki ayrı kamera oturumuna alınır (birinci oturumda sol bacak, ikinci oturumda sağ bacak kameraya yakın tarafa bakar). Her oturumda aşağıdaki 3 görev gerçekleştirilir:

### Görev 1: Squat (Çömelme)
- **Tekrar:** Rahat ve doğal tempoda 3 tam tekrar.
- **Başlangıç:** Ayaklar omuz genişliğinde açık, dik duruş (0° referansı).
- **Hareket:** Dizler yaklaşık 90° fleksiyona gelene kadar kontrollü çöküş ve ardından dik konuma dönüş.
- **Dinlenme:** Tekrarlar arası 5 saniye, görevler arası 1 dakika dinlenme.

### Görev 2: Oturup Kalkma (Sit-to-Stand)
- **Tekrar:** Standart yükseklikteki kolçaksız sandalyeden 3 tekrar.
- **Başlangıç:** Sandalyede dik oturuş pozisyonu.
- **Hareket:** Destek almadan ayağa kalkış, 2 saniye dik duruş ve tekrar kontrollü oturma.

### Görev 3: Düz Hat Üzerinde Yürüme (Gait)
- **Tekrar:** 5 metre uzunluğundaki düz parkurda 5 geçiş.
- **Kapsam:** Kamera kadrajından geçerken yaklaşık 1-2 tam adım döngüsü (stride cycle) kaydedilir.

---

## 5. Kalibrasyon ve Veri Toplama Adımları

1. **Açılış Kontrolü:** ESP32 batarya seviyesi ölçülür, Bluetooth SPP bağlantısı kurulur.
2. **Sıfır Referansı (`Z` Komutu):** Katılımcı dik ve düz duruşta beklerken `Z` komutu gönderilir. Enkoder sayaçları sıfırlanır, eşzamanlı olarak kameradaki bacak açısı başlangıç ofseti olarak kaydedilir.
3. **Kayıt Başlatma (`S` Komutu):** Hareket öncesinde kayıt tetiklenir; 50 Hz enkoder paketleri ve 30 FPS kamera kareleri diske yazılır.
4. **Kayıt Durdurma (`P` Komutu):** Hareket tamamlandıktan sonra akış durdurulur ve CSV oturum dosyası kaydedilir.
5. **Kalite Kontrol:** Landmark görünürlük ortalaması ($v \ge 0.6$) ve paket kayıp oranı kontrol edilir; kayma veya perdelenme olan tekrarlar not edilir.
