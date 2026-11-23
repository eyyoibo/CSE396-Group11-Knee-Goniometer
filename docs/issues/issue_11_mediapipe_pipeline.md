---
title: "[M3] 1080p@30FPS OpenCV Kamera Akisi ve MediaPipe Pose Hatti"
labels: ["module-3", "software", "priority-high"]
milestone: "M3-Camera Pipeline"
assignees: ["Mert Canoglu", "Cem Baygin"]
---

## 📌 Is Tanimi
Tripod uzerinde sagittal duzlemde konumlandirilmis kameradan OpenCV ile 1080p @ 30 FPS goruntu alinacak; yerel bilgisayarda calisan onceden egitilmis **MediaPipe Pose (BlazePose)** modeli ile kalca, diz ve ayak bilegi anahtar noktalarinin 2B normalize piksel koordinatlari ve gorunurluk skorlari cikarilacaktir.

## 🎯 Kabul Kriterleri
- [ ] OpenCV `VideoCapture` ile baglanti acilmali, hedef 1920x1080 ve 30 FPS teyit edilmeli.
- [ ] Her kare BGR'den RGB'ye cevrilerek MediaPipe Pose modeline beslenmeli (`model_complexity=1`).
- [ ] Kameraya yakin olan bacagin landmarklari alinmali:
  - Sol Bacak: `LEFT_HIP (23)`, `LEFT_KNEE (25)`, `LEFT_ANKLE (27)`
  - Sag Bacak: `RIGHT_HIP (24)`, `RIGHT_KNEE (26)`, `RIGHT_ANKLE (28)`
- [ ] Her nokta icin `(x, y, visibility)` cikarilmali; `visibility < 0.6` olan kareler gecersiz olarak isaretlenmeli.
- [ ] Uctan uca isleme hizi yerel bilgisayarda en az 25 FPS olmali; gecikme raporlanmali.

## 📋 Alt Gorevler
- [ ] `module3_mediapipe_simulation/src/camera_capture.py` icindeki `start()` ve `read_frame()` fonksiyonlarini gercekle.
- [ ] `module3_mediapipe_simulation/src/pose_detector.py` icindeki landmark cikarma mantigini tamamla.
