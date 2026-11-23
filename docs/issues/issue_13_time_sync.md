---
title: "[M3] Donanim Zaman Damgasi ile Zaman Eşleştirme ve İnterpolasyon"
labels: ["module-3", "module-2", "software", "priority-high"]
milestone: "Integration"
assignees: ["Ibrahim Halil Dogan", "Mert Canoglu"]
---

## 📌 Is Tanimi
Kamera akisi 30 FPS (~33.3 ms aralikli) ve ESP32 enkoder akisi 50 Hz (20 ms aralikli) farkli frekanslarda calismaktadir. Gecerli ve adil bir RMSE karsilastirmasi yapabilmek icin, iki sinyal ayni zaman eksenine getirilmeli ve dogrusal interpolasyon uygulanmalidir.

## 🎯 Kabul Kriterleri
- [ ] ESP32'den gelen gonderici zaman damgasi ($t_{ESP}$) ile bilgisayarin monotonik saati ($t_{PC}$) arasindaki baslangic saat farki $\Delta t_{offset}$ hesaplanmali.
- [ ] Kamera aci serisi, enkoder zaman damgalarina `np.interp` kullanilarak dogrusal interpole edilmeli.
- [ ] Gorunurluk esigi altinda kalan gecersiz kareler interpolasyon disinda tutulup `NaN` olarak isaretlenmeli.
- [ ] Kontrollu periyodik diz bukme hareketi ile capraz korelasyon (cross-correlation) yapilarak artik zaman gecikmesinin 1 kamera karesi ($\le 33\text{ ms}$) icinde kaldigi dogrulanmali.

## 📋 Alt Gorevler
- [ ] `module3_mediapipe_simulation/src/angle_calculator.py` icindeki `interpolate_to_encoder_timestamps()` metodunu gercekle.
- [ ] Senkronizasyon dogrulugu icin test senaryolari olustur.
