# Test Altyapisi

Bu dizin, projenin birim testlerini icerir. Testler `pytest` ile calistirilir.

## Test Dosyalari

| Dosya | Test Ettigi Modul | Aciklama |
|-------|-------------------|----------|
| `test_packet_parser.py` | Shared | Paket cozumleme, CRC dogrulama, hata durumlari |
| `test_angle_calculator.py` | Modul 3 | Vektor aci hesabi, filtre, enterpolasyon |
| `test_analysis_engine.py` | Modul 2 | RMSE/MAE hesaplama, Bland-Altman |

## Calistirma

```bash
# Tum testleri calistir
pytest tests/ -v

# Belirli bir test dosyasini calistir
pytest tests/test_packet_parser.py -v

# Kapsam raporu ile
pytest tests/ --cov=shared --cov=module2_interface_rmse --cov=module3_mediapipe_simulation
```

## Test Yazim Kurallari

- Her yeni fonksiyon icin en az bir basarili ve bir basarisiz test senaryosu yazin
- Fiziksel donanim gerektiren testleri `@pytest.mark.hardware` ile isaretleyin
- Kamera gerektiren testleri `@pytest.mark.camera` ile isaretleyin
- Bilinen aci degerleriyle dogruluk testleri olusturun
