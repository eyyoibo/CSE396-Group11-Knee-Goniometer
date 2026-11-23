---
title: "[M3] 2D Şematik Bacak Simülasyonu ve Canli Bilgi Paneli"
labels: ["module-3", "software", "priority-medium"]
milestone: "M3-Camera Pipeline"
assignees: ["Cem Baygin", "Mert Canoglu"]
---

## 📌 Is Tanimi
Video karesi uzerine iki boyutlu sematik bacak cizimi (uyluk ve baldir dogru parcalari), diz eklem acisi yayi ve sag ust kosede yari saydam bilgi paneli (anlik aci, gorunurluk puani, anlik FPS) gercek zamanli olarak bindirilecektir (overlay).

## 🎯 Kabul Kriterleri
- [ ] Kalca-diz ve diz-ayak bilegi noktalari arasinda kemik cizgileri (`cv2.line`) ve eklem cemberleri (`cv2.circle`) cizilmeli.
- [ ] Diz noktasi merkezli dairesel aci yayi (`cv2.ellipse`) hesaplanan aci genisliginde cizilmeli.
- [ ] Yari saydam bilgi paneli icinde:
  - Anlik Diz Acisi: `XX.X°`
  - Landmark Gorunurluk Puani: `0.XX`
  - Anlik Kamera FPS: `XX`
- [ ] Aciklama: Bu cizim yalnizca olculen aciyi temsil eden sematik bir gosterimdir; 3B anatomik biyomekanik model veya klinik tani araci iddiasi tasimaz.

## 📋 Alt Gorevler
- [ ] `module3_mediapipe_simulation/src/simulation_renderer.py` icindeki `draw_skeleton_overlay`, `draw_angle_arc` ve `draw_info_panel` metodlarini tamamla.
- [ ] OpenCV penceresinde cizim gecikmesini en aza indirecek sekilde optimize et.
