---
title: "[M2] Bland-Altman Uyum Analizi ve %95 Uyum Sinirlari Görselleştirmesi"
labels: ["module-2", "software", "priority-medium"]
milestone: "M2-Desktop MVP"
assignees: ["Cem Baygin", "Mert Canoglu"]
---

## 📌 Is Tanimi
Kamera tabanli isaretleyicisiz olcum ile enkoder mekanik olcumu arasindaki klinik/teknik uyumu degerlendirmek uzere Bland-Altman analiz algoritmasi ve grafik cizimi gelistirilecektir.

## 🎯 Kabul Kriterleri
- [ ] Her ornek cifti icin ortalama: $S_i = \frac{\theta_{kamera}(t_i) + \theta_{enkoder}(t_i)}{2}$
- [ ] Her ornek cifti icin fark: $D_i = \theta_{kamera}(t_i) - \theta_{enkoder}(t_i)$
- [ ] Ortalama fark (Bias): $\bar{D} = \frac{1}{N}\sum D_i$
- [ ] Farklarin standart sapmasi ($SD$) hesaplanmali.
- [ ] %95 Uyum Sinirlari (Limits of Agreement - LoA):
  $$\text{Ust Sinir} = \bar{D} + 1.96 \cdot SD$$
  $$\text{Alt Sinir} = \bar{D} - 1.96 \cdot SD$$
- [ ] Oturum bittiginde veya toplu analizde Matplotlib ile sacilim grafigi olusturulup PNG formatinda kaydedilebilmeli.
- [ ] Ayni katilimcidan alinan tekrarlarin bagimsiz olmadigi gozetilerek Bland ve Altman (2007) yontemine uygun agirlikli varyans hesaplama destegi saglanmali.

## 📋 Alt Gorevler
- [ ] `module2_interface_rmse/src/analysis_engine.py` icindeki `compute_bland_altman` metodunu yaz.
- [ ] Sentetik verilerle unit testini gerceklestir.
