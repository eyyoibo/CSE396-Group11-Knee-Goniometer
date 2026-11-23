---
title: "[M2] Gerçek Zamanli PyQtGraph Canli Grafikleri"
labels: ["module-2", "software", "priority-medium"]
milestone: "M2-Desktop MVP"
assignees: ["Mert Canoglu"]
---

## 📌 Is Tanimi
PyQtGraph kutuphanesi kullanilarak, yuksek performansli 3 adet canli zaman serisi grafigi cizilecektir:
1. **Aci - Zaman Grafigi ($\theta(t)$):** Sol diz enkoder acisi (mavi), sag diz enkoder acisi (yesil) ve kameraya yakin diz icin MediaPipe acisi (kirmizi kesikli).
2. **Birikimli Sayim Grafigi ($N(t)$):** Sol ve sag enkoder birikimli darbe sayisi.
3. **Ornekler Arasi Sayim Artisi ($\Delta N(t) = N(t) - N(t-1)$):** Anlik acisal hiz gostergesi.

## 🎯 Kabul Kriterleri
- [ ] PyQtGraph `PlotWidget` bilesenleri kullanilarak grafik guncellemeleri 30-50 FPS'te akici sekilde calismali.
- [ ] X ekseninde kayan son 10 saniyelik zaman penceresi gosterilmeli; Y ekseni 0°-150° araliginda olceklenmeli.
- [ ] Grafik cizimi veri alim thread'ini yavaslatmamali; `QTimer` ile ~30 Hz arayuz yenileme uygulanmali.
- [ ] Eksen etiketleri, birimler ve gosterge (legend) alanlari anlasilir olmali.

## 📋 Alt Gorevler
- [ ] `main_window.py` icine 3 plot panelini yerlestir.
- [ ] `update_plots()` metodunda dairesel tampon (circular buffer / deque) kullanarak veriyi ciz.
