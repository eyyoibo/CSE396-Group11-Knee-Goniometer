---
title: "[M1] Gömülü Yazilimda Sayim-Aci Katsayisi ve Sifirlama Kalibrasyonu"
labels: ["module-1", "software", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Ibrahim Halil Dogan", "Cem Baygin"]
---

## 📌 Is Tanimi
ESP32 uzerinde donanimsal sayicidan okunan anlik sayim degerleri ($N(t)$), onceden belirlenen mekanik aktarim ve cozunurluk katsayisiyla carpilarak gercek diz acisina ($\theta$) donusturulecektir. Ayrica 'Z' komutu ile sifirlama ofseti dinamik olarak hesaplanacaktir.

## 🎯 Kabul Kriterleri
- [ ] Aci donusum formulu: $\theta = (N - N_{offset}) \times \frac{360.0}{20000.0} = (N - N_{offset}) \times 0.018^\circ$ olarak gerceklenmeli.
- [ ] 'Z' komutu geldiginde $N_{offset} = N_{anlik}$ yapilmali ve telemetri paketindeki aci degeri $0.0^\circ$ olmali.
- [ ] Ters yone bukulme durumunda negatif acilar veya 0-180 derece araliginda sinirlandirma (clamping) secenegi saglanmali.
- [ ] 0°, 30°, 60°, 90°, 120° referans tezgâh olcumlerinde ortalama mutlak hata $\le 2^\circ$ olmali.

## 📋 Alt Gorevler
- [ ] `calculate_angle_from_counts()` fonksiyonunu `main.c` icinde tamamla.
- [ ] Tezgâh testi verilerini kaydet ve tezgâh katsayisini raporla.
