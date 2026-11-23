---
title: "[M2] Kayan Pencere (5s) MAE/RMSE ve Tepe Aci Farki Analiz Motoru"
labels: ["module-2", "software", "priority-high"]
milestone: "M2-Desktop MVP"
assignees: ["Ibrahim Halil Dogan", "Cem Baygin"]
---

## 📌 Is Tanimi
Enkoder aci serisi ile kameradan elde edilen ve ayni zaman eksenine hizalanmis kamera aci serisi arasindaki olcum farklari; canli olcum sirasinda son 5 saniyelik kayan pencere uzerinde, oturum sonunda ise tum gecerli kayit icin istatistiksel metriklerle hesaplanacaktir.

## 🎯 Formüller ve Kabul Kriterleri
- [ ] **Ortalama Mutlak Hata (MAE):**
  $$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |\theta_{kamera}(t_i) - \theta_{enkoder}(t_i)|$$
- [ ] **Kök Ortalama Kare Hata (RMSE):**
  $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (\theta_{kamera}(t_i) - \theta_{enkoder}(t_i))^2}$$
- [ ] **Ortalama Sapma (Bias, $\bar{d}$):**
  $$\bar{d} = \frac{1}{N} \sum_{i=1}^{N} (\theta_{kamera}(t_i) - \theta_{enkoder}(t_i))$$
- [ ] **Tepe Aci Farki ($\Delta\theta_{peak}$):** Hareketin tepe noktasindaki (maksimum fleksiyon) mutlak aci farki.
- [ ] MediaPipe tarafindan gecersiz (visibility < 0.6) olarak isaretlenen kareler hata hesabina katilmamali, gecersiz kare orani ayrica hesaplanmali.
- [ ] Arayuz sag panelindeki LED/etiket kutularinda bu metrikler canli guncellenmeli.

## 📋 Alt Gorevler
- [ ] `module2_interface_rmse/src/analysis_engine.py` icinde `compute_sliding_rmse` ve `compute_sliding_mae` metodlarini gercekle.
- [ ] `tests/test_analysis_engine.py` unit testlerini calistirip dogrula.
