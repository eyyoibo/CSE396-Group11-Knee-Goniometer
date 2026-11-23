---
title: "[M1] Bluetooth Classic SPP Iletisim Katmani ve Z/S/P Durum Makinesi"
labels: ["module-1", "software", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Ibrahim Halil Dogan"]
---

## 📌 Is Tanimi
ESP32 uzerinde Bluetooth Classic SPP (Serial Port Profile / RFCOMM) sunucusu kurulacak; 50 Hz hassas frekansta 28 baytlik ikili telemetri paketleri gonderilecek ve masaustu/mobil istemciden gelen tek baytlik ASCII komutlar (`Z`, `S`, `P`) donanim durum makinesinde islenecektir.

## 🎯 Kabul Kriterleri
- [ ] ESP-IDF `esp_spp_api.h` ve `esp_bt_main.h` kutuphaneleri ile SPP sunucu baslatilmali (`Device Name: ESP32_GONIOMETER`).
- [ ] FreeRTOS periyodik gorevi (timer) ile 20 ms araliklarla ($50\text{ Hz}$) telemetri paketi uretilip sokete yazilmali.
- [ ] 5 dakikalik kesintisiz gonderim testinde ortalama iletim hizi $\ge 48\text{ Hz}$ ve paket kaybi $<\%1$ olmali.
- [ ] Gelen ASCII karakterleri:
  - `'Z'`: Enkoder birikimli ofsetini sifirla.
  - `'S'`: Telemetri akisini baslat (`STATE_STREAMING`).
  - `'P'`: Telemetri akisini dondur (`STATE_PAUSED`).

## 📋 Alt Gorevler
- [ ] `module1_hardware_encoder/src/main.c` icinde `bluetooth_spp_init()` ve `send_telemetry_packet()` fonksiyonlarini gercekle.
- [ ] 28 baytlik paket icin CRC-16/CCITT kontrol fonksiyonunu uygula.
- [ ] Baglanti kopmasi durumunda otomatik yeniden dinleme moduna gecisi sagla.
