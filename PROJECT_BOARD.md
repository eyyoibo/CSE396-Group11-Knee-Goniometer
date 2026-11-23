# GitHub Proje Panosu Kurulum Rehberi

Bu belge, projenin GitHub Projects panosunun nasıl oluşturulacağını ve etkin bir şekilde kullanılacağını açıklar.

## Kanban Panosu Oluşturma

### Adımlar

1. GitHub deposunda **Projects** sekmesine gidin
2. **New project** butonuna tıklayın
3. **Board** (Pano) şablonunu seçin
4. Proje adı olarak **"Diz Gonyometresi — Geliştirme Panosu"** girin
5. Aşağıdaki sütunları oluşturun

### Sütun Tanımları

| Sütun | Açıklama | Kullanım |
|-------|----------|----------|
| **Backlog** | Tanımlanmış ancak henüz planlanmamış görevler | Yeni issue'lar buraya düşer |
| **To Do** | Mevcut sprint için planlanmış görevler | Sprint planlamasında buraya taşınır |
| **In Progress** | Üzerinde aktif olarak çalışılan görevler | Geliştirici işe başladığında buraya taşır |
| **Review** | Kod gözden geçirme bekleyen görevler | PR açıldığında buraya taşınır |
| **Done** | Tamamlanmış ve birleştirilmiş görevler | PR onaylanıp birleştirilince buraya geçer |

## Etiket (Label) Tanımları

Aşağıdaki etiketleri depo ayarlarından oluşturun:

### Modül Etiketleri

| Etiket | Renk | Açıklama |
|--------|------|----------|
| `module-1` | `#1d76db` (mavi) | Donanım ve Gömülü Yazılım (ESP32, encoder) |
| `module-2` | `#0e8a16` (yeşil) | Masaüstü Arayüz (PyQt6 GUI) |
| `module-3` | `#d93f0b` (kırmızı) | Kamera ve Görüntü İşleme (MediaPipe) |
| `module-4` | `#5319e7` (mor) | Mobil Uygulama (React Native) |

### Tür Etiketleri

| Etiket | Renk | Açıklama |
|--------|------|----------|
| `bug` | `#d73a4a` (koyu kırmızı) | Hata raporu |
| `enhancement` | `#a2eeef` (açık mavi) | Yeni özellik veya iyileştirme |
| `documentation` | `#0075ca` (koyu mavi) | Dokümantasyon değişikliği |
| `hardware` | `#f9d0c4` (açık turuncu) | Donanımla ilgili konu |
| `software` | `#c5def5` (açık mavi) | Yazılımla ilgili konu |
| `testing` | `#bfd4f2` (soluk mavi) | Test ekleme veya güncelleme |

### Öncelik Etiketleri

| Etiket | Renk | Açıklama |
|--------|------|----------|
| `priority-high` | `#b60205` (kırmızı) | Acil — hemen ele alınmalı |
| `priority-medium` | `#fbca04` (sarı) | Orta — mevcut sprintte çözülmeli |
| `priority-low` | `#0e8a16` (yeşil) | Düşük — zaman buldukça ele alınabilir |

## Kilometre Taşları (Milestones)

Aşağıdaki kilometre taşlarını oluşturun:

### M1 — Donanım Prototipi
**Hedef:** Encoder'lar ve ESP32 ile temel veri iletimi çalışır durumda
- Encoder sürücüsü yazıldı ve test edildi
- Bluetooth SPP ve BLE iletişimi kuruldu
- 28 baytlık paket formatı tanımlandı ve uygulandı
- Temel donanım prototipi monte edildi

### M2 — Masaüstü MVP
**Hedef:** Masaüstü uygulamanın minimum uygulanabilir ürünü hazır
- Bluetooth üzerinden veri alımı çalışıyor
- Gerçek zamanlı açı grafiği görüntüleniyor
- CSV'ye veri kaydı yapılabiliyor
- Temel kalibrasyon arayüzü mevcut

### M3 — Kamera İşlem Hattı
**Hedef:** Kamera tabanlı açı ölçümü çalışır durumda
- Kamera yakalama ve önizleme çalışıyor
- MediaPipe Pose entegrasyonu tamamlandı
- Açı hesaplama doğrulandı
- M2 ile entegrasyon sağlandı (yan yana görüntüleme)

### M4 — Mobil Uygulama
**Hedef:** Mobil uygulama temel işlevleriyle hazır
- BLE bağlantı yönetimi çalışıyor
- Gerçek zamanlı açı görüntüleme mevcut
- Oturum geçmişi kaydediliyor

### Entegrasyon
**Hedef:** Tüm modüller birlikte çalışıyor
- Encoder ve kamera verileri zaman eşleştirmeli karşılaştırma
- Uçtan uca test senaryoları geçiyor
- Performans optimizasyonu tamamlandı

### Final Raporu
**Hedef:** Proje teslime hazır
- Teknik rapor yazıldı
- Kullanım kılavuzu hazırlandı
- Sunum materyalleri tamamlandı
- Kod temizliği ve son gözden geçirme yapıldı

## Panoyu Etkin Kullanma

### Günlük İş Akışı

1. **Sabah:** Panonun **In Progress** sütununu kontrol edin, üzerinde çalıştığınız görevlerin güncel olduğundan emin olun
2. **İş sırasında:** Görev durumunu değiştirdiğinizde kartı uygun sütuna taşıyın
3. **PR açtığınızda:** İlgili kartı **Review** sütununa taşıyın
4. **Gün sonu:** Tamamlanan görevlerin **Done** sütununa geçtiğini doğrulayın

### Issue Oluşturma İpuçları

- Her issue'ya en az bir **modül etiketi** ekleyin
- **Öncelik etiketi** eklemeyi unutmayın
- İlgili **kilometre taşını** seçin
- Mümkünse kendiniziatayanlar (assignee) olarak ekleyin
- Bağımlılıkları issue açıklamasında belirtin

### Sprint Kartını Doldurmak

Her sprint başında **Backlog** sütunundan **To Do** sütununa taşınacak görevleri seçin. Seçim kriterleri:
- Öncelik sırası
- Bağımlılık ilişkileri (ön koşullar tamamlanmış olmalı)
- Takım üyelerinin uygunluğu
- Sprint kapasitesi (aşağıdaki önerilere bakın)

## Sprint Planlama Önerileri

Projenin zamanına ve kapsamına uygun olarak **2 haftalık sprintler** önerilmektedir.

### Sprint Yapısı

| Gün | Etkinlik |
|-----|----------|
| **1. gün (Pazartesi)** | Sprint planlama toplantısı (30-45 dk) |
| **2-9. gün** | Geliştirme çalışması |
| **10. gün (Cuma)** | Sprint kapanış ve retrospektif (30 dk) |

### Sprint Planlama Toplantısı Gündemi

1. Önceki sprintin **Done** sütunundaki görevleri gözden geçirin
2. Tamamlanamayan görevlerin nedenlerini tartışın
3. Yeni sprint için **Backlog**'dan görev seçin
4. Her görev için sorumlu atayın
5. Bağımlılıkları ve riskleri belirleyin

### Kapasite Önerisi

3 kişilik takım için sprint başına önerilen iş yükü:

| Efor | Puan | Sprint Başına Hedef |
|------|------|---------------------|
| **S (Küçük)** | 1 puan | Toplam 8-10 küçük görev |
| **M (Orta)** | 3 puan | Toplam 3-4 orta görev |
| **L (Büyük)** | 5 puan | Toplam 1-2 büyük görev |

**Hedef sprint puanı:** Takım için toplam ~20-25 puan

> **İpucu:** İlk birkaç sprintte hedefi düşük tutun ve takımın hızını ölçerek sonraki sprintlerde ayarlayın.
