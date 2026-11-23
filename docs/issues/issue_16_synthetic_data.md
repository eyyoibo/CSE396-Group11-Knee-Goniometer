---
title: "[Shared] Donanimsiz Test için Sentetik Telemetri Paketi Üreteci"
labels: ["testing", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Ibrahim Halil Dogan", "Mert Canoglu"]
---

## 📌 Is Tanimi
Fiziksel ESP32 donanimi ve enkoderler henuz tezgâhta lehimlenirken veya hazir degilken; Modül 2 (masaustu GUI) ve Modül 3 (zaman eslestirme) gelistirmelerinin aksamamasi icin gercekci diz fleksiyonu (squat) hareketini simule eden sentetik paket ureteci gelistirilecektir.

## 🎯 Kabul Kriterleri
- [ ] Parametreler: Paket frekansi (50 Hz), hareket periyodu (or. 2 sn periyotlu 0°-90° squat sinus egrisi), gaussyen gurultu ($\sigma = 0.3^\circ$).
- [ ] Cikti: Tam 28 baytlik ikili paket (`0xAA 0x55`, artan sira no, ms zaman damgasi, sol/sag sayim, sol/sag aci, CRC16).
- [ ] Iletim Kanali: Sanal seri port (Windows com0com / Linux pty) veya yerel TCP soket (127.0.0.1:9000).
- [ ] Donanim olmadan masaustu uygulamasinin acilip tum grafiklerin ve RMSE hesaplamasinin sentetik veriyle dogrulanabilmesi.

## 📋 Alt Gorevler
- [ ] `shared/synthetic_data_generator.py` icindeki `generate_angle`, `build_packet` ve `run_serial` fonksiyonlarini tamamla.
- [ ] `shared/packet_parser.py` ile entegrasyon testini yap.
