---
title: "[M2] Bluetooth Seri Veri Alici QThread ve Paket Ayrıştırıcı"
labels: ["module-2", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Ibrahim Halil Dogan"]
---

## 📌 Is Tanimi
PyQt6 ana arayuzunun (UI thread) donmasini onlemek amaciyla, Bluetooth SPP seri portundan gelen 50 Hz telemetri paketlerini ayri bir arka plan is parcaciginda (`QThread`) okuyup dogrulayacak ve basarili paketleri sinyallerle arayuze iletecek alici sinif gelistirilecektir.

## 🎯 Kabul Kriterleri
- [ ] `pyserial` ile acilan seri porttan non-blocking bayt okuma gerceklestirilmeli.
- [ ] Gelen tamponda `0xAA 0x55` basligi aranmali, 28 bayt tamamlandiginda `shared/packet_parser.py` ile cozumleme yapilmali.
- [ ] CRC16 kontrolu basarisiz paketler veya sira numarasi atlamalari (packet loss) tespit edilip loglanmali.
- [ ] Her gecerli pakette `new_packet_received(TelemetryPacket)` Qt sinyali yayinlanmali.
- [ ] Baglanti koptugunda arayuz kilitlenmeden hata sinyali uretilmeli ve temiz kapanis saglanmali.

## 📋 Alt Gorevler
- [ ] `module2_interface_rmse/src/bluetooth_receiver.py` sinifinin `run()` dongusunu gercekle.
- [ ] Sentetik veri ureteci ile 50 Hz paket akisini test et.
