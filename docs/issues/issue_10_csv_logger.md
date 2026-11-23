---
title: "[M2] Senkronize Çok Sütunlu CSV Veri Kayit Sistemi"
labels: ["module-2", "software", "priority-medium"]
milestone: "M2-Desktop MVP"
assignees: ["Ibrahim Halil Dogan"]
---

## 📌 Is Tanimi
Masaustu uygulamasinda 'S' (Start) ile baslatilip 'P' (Pause) ile durdurulan her olcum oturumu; anlik zaman damgalari, ham enkoder sayimlari, hesaplanan acilar, MediaPipe landmark koordinatlari ve gorunurluk skorlarini iceren standart bir CSV dosyasina yazilacaktir.

## 🎯 Kabul Kriterleri
- [ ] Dosya isimlendirme sablonu: `session_YYYYMMDD_HHMMSS_<KatilimciKodu>_<Gorev>.csv`
- [ ] Sutun basliklari:
  `timestamp_ms, seq_num, enc_left_count, enc_right_count, enc_left_deg, enc_right_deg, cam_deg, cam_visibility, valid_flag`
- [ ] Disk yazma islemi arayuzu kilitmemek icin tamponlu (buffered writing) ve periyodik flush ile yapilmali.
- [ ] 'P' komutuna basildiginda veya uygulama kapatildiginda tum tampon diske bosaltilip dosya temiz kapatilmali.

## 📋 Alt Gorevler
- [ ] `module2_interface_rmse/src/csv_logger.py` sinifini tamamla.
- [ ] Örnek CSV dosyasini olusturup `shared/sample_session.csv` referansiyla karsilastir.
