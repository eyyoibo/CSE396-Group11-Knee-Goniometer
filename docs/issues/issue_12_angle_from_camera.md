---
title: "[M3] Vektörel Diz Açisi Hesabi ve Butterworth Düşük Geçişli Filtreleme"
labels: ["module-3", "software", "priority-high"]
milestone: "M3-Camera Pipeline"
assignees: ["Mert Canoglu"]
---

## 📌 Is Tanimi
Tespit edilen kalca ($P_{hip}$), diz ($P_{knee}$) ve ayak bilegi ($P_{ankle}$) koordinatlarindan vektor ic acisi kullanilarak diz fleksiyon acisi hesaplanacak; ardindan kamera titremelerini (jitter) onlemek amaciyla dusuk karmasiklikli Butterworth filtresi uygulanacaktir.

## 🎯 Kabul Kriterleri
- [ ] Vektorler:
  $$\vec{u} = P_{hip} - P_{knee}$$
  $$\vec{v} = P_{ankle} - P_{knee}$$
- [ ] Ic Aci Formulu:
  $$\alpha = \arccos\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}\right)$$
- [ ] Diz Fleksiyon Acisi: $\theta_{kamera} = 180^\circ - \alpha$ (Tam duz bacak konumu $0^\circ$).
- [ ] Sayisal kararlilik icin kosinus degeri $[-1.0, 1.0]$ araligina kirpilmali (`np.clip`).
- [ ] 2. dereceden dusuk gecisli Butterworth filtresi ($f_c \approx 6\text{ Hz}$, $f_s = 30\text{ Hz}$) ile yuksek frekansli gurultu bastirilmali.
- [ ] Tezgâh uzerinde bilinen sabit acili kaliplarla (0°, 45°, 90°, 120°) aci hesabi dogrulanmali.

## 📋 Alt Gorevler
- [ ] `module3_mediapipe_simulation/src/angle_calculator.py` icindeki `compute_angle()` ve `apply_butterworth_filter()` metodlarini yaz.
- [ ] `tests/test_angle_calculator.py` birim testlerinin basariyla gectigini teyit et.
