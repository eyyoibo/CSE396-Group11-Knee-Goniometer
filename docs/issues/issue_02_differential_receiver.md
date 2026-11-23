---
title: "[M1] Diferansiyel Alici Devre Tasarimi ve Baglantisi"
labels: ["module-1", "hardware", "priority-high"]
milestone: "M1-Hardware Prototype"
assignees: ["Cem Baygin", "Mert Canoglu"]
---

## 📌 Is Tanimi
Enkoderlerden gelen uzun kablolu diferansiyel sinyaller ($A, \bar{A}, B, \bar{B}$) ortamdaki elektromanyetik gurultulere aciktir. Bu sinyallerin gurultuden arindirilmasi ve ESP32'nin 3.3V CMOS lojik giris seviyesine guvenle donusturulmesi icin **AM26C32** (veya muadili) 4 kanalli diferansiyel hat alici entegresi iceren ara devre tasarlanacak ve baglantilari yapilacaktir.

## 🎯 Kabul Kriterleri
- [ ] Sol ve sag enkoder diferansiyel hatlari AM26C32 girislerine baglanmali, 120 Ohm hat sonlandirma direcleri eklenmeli.
- [ ] Alici entegre cikislarinin 3.3V lojik gerilimi asmadigi multimetre ve osiloskop ile olculmeli.
- [ ] ESP32 ve enkoder sase (GND) hatlari tek noktadan baglanarak toprak donguleri (ground loop) engellenmeli.
- [ ] Devre semasi ve baglanti pin tablosu `module1_hardware_encoder/docs/WIRING.md` dokumanina eklenmeli.

## 📋 Alt Gorevler
- [ ] Delikli plaket uzerinde prototip devre lehimlemesi yap.
- [ ] Hizli hareket sirasinda A ve B fazlari arasindaki 90° faz farkini lojik analizor ile teyit et.
- [ ] Bel kemerine monte edilecek korumali kutu icine montaj plani cikar.
