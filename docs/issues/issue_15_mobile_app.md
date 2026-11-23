---
title: "[M4] Mobil Uygulama Geliştirme (Kadran, Bluetooth ve Z/S/P Kontrolü)"
labels: ["module-4", "software", "priority-low"]
milestone: "M4-Mobile App"
assignees: ["Ibrahim Halil Dogan"]
---

## 📌 Is Tanimi
Kullanicinin/fizyoterapistin saha testlerinde bilgisayar tasimadan diz eklem acisini izlemesi, hastaya anlik geri bildirim vermesi ve Z/S/P komutlariyla olcumu yonetmesi icin React Native / TypeScript tabanli mobil uygulama gelistirilecektir.

## 🎯 Kabul Kriterleri
- [ ] Bluetooth Classic SPP veya BLE baglanti yonetimi (otomatik arama, baglanma ve kopma durumunda uyari).
- [ ] Gosterge Paneli (Dashboard): 0°-150° araliginda renkli analog kadran (gauge) uzerinde anlik aci ve sayisal deger gosterimi.
- [ ] Kontrol Ekrani:
  - 'Z' Butonu (Sifirlama kalibrasyonu)
  - 'S' Butonu (Olcumu baslatma)
  - 'P' Butonu (Olcumu duraklatma)
- [ ] Gecmis Ekrani: Seans suresi, tepe aci (ROM) ve CSV formatinda yerel depolama/paylasma secenegi.

## 📋 Alt Gorevler
- [ ] `module4_mobile_app/src/services/BluetoothService.ts` icinde baglanti mantigini tamamla.
- [ ] `module4_mobile_app/src/components/AngleGauge.tsx` icinde SVG ibre rotasyonunu bagla.
- [ ] Android fiziki cihaz uzerinde Bluetooth SPP paket akisini test et.
