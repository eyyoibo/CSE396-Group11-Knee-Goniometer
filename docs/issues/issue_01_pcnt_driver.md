---
title: "[M1] ESP32 PCNT Donanim Sayici Surucu Kurulumu"
labels: ["module-1", "hardware", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Cem Baygin", "Ibrahim Halil Dogan"]
---

## 📌 Is Tanimi
ESP32 mikrodenetleyicisi uzerindeki donanimsal **PCNT (Pulse Counter)** cevre birimi yapilandirilarak, her iki dizlik uzerindeki 5000 PPR optik/manyetik artimli enkoderlerin A/B diferansiyel sinyallerinin 4x kuadratur cozme modunda CPU'ya ek yuk getirmeden sayilmasi saglanacaktir.

## 🎯 Kabul Kriterleri
- [ ] ESP-IDF `driver/pulse_cnt.h` API'si kullanilarak Sol Diz (PCNT Unit 0) ve Sag Diz (PCNT Unit 1) tanimlanmali.
- [ ] 4 kenar tetikleme (EDGE_RISING / EDGE_FALLING) ile 1 devirde $5000 \times 4 = 20.000$ sayim dogrulanmali ($\approx 0.018^\circ$ cozunurluk).
- [ ] Sayici tasmasi (overflow / underflow, 16-bit donanim limiti: -32768 ile +32767) durumunda kesme (ISR) uretilmeli ve 32-bit birikimli sayac (`int32_t`) kesintisiz guncellenmeli.
- [ ] Gecici gurultuleri onlemek icin PCNT donanimsal filtreleme suresi (glitch filter, ~1 us) aktif edilmeli.
- [ ] Sayaçlari anlik okuyan `pcnt_get_counts(int32_t *left, int32_t *right)` fonksiyonu gerceklenmeli.

## 📋 Alt Gorevler
- [ ] `module1_hardware_encoder/include/config.h` icinde GPIO pinlerini belirle.
- [ ] `module1_hardware_encoder/src/main.c` icinde `pcnt_init_encoders()` fonksiyonunu tamamla.
- [ ] Tezgâhta enkoder mili 1 tam tur donduruldugunde tam 20.000 sayim alindigini osiloskop/seri port ile dogrula.
