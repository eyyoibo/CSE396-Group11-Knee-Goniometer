---
title: "[M2] PyQt6 Masaüstü Arayüz Iskeleti ve Panel Düzeni"
labels: ["module-2", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Mert Canoglu", "Ibrahim Halil Dogan"]
---

## 📌 Is Tanimi
Masaustunde calisacak Python PyQt6 tabanli kullanici arayuzunun (GUI) ana pencere duzeni kurulacaktir. Arayuz; sol tarafta baglanti ve oturum kontrollerini, ortada canli grafikleri, sag tarafta ise anlik hata metriklerini (RMSE/MAE) ve kamera goruntusunu barindiracaktir.

## 🎯 Kabul Kriterleri
- [ ] `QMainWindow` temelinde responsive ve modern karanlik tema (Dark Theme) stili olusturulmali.
- [ ] Ust Arac Cubugu (Toolbar): Port secim kutusu (COM port / RFCOMM), "Baglan/Kes", "Sifirla [Z]", "Baslat [S]", "Durdur [P]", "CSV Disa Aktar" butonlari yer almali.
- [ ] Klavye kisayollari ('Z', 'S', 'P') tanimlanmali.
- [ ] Durum cubugunda (StatusBar): Baglanti durumu, anlik paket hizi (Hz), oturum suresi ve dosya yazma durumu goruntulenmeli.

## 📋 Alt Gorevler
- [ ] `module2_interface_rmse/src/main_window.py` sinifinin `init_ui()` fonksiyonunu tamamla.
- [ ] Qt sinyalleri ile butonlarin arkasindaki islevleri (slot) bagla.
