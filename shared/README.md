# Paylasilan Yardimci Araclar (Shared Utilities)

Bu dizin, birden fazla modul tarafindan ortaklasa kullanilan yardimci arac ve betikleri icerir.

## Dosyalar

### packet_parser.py
ESP32 tarafindan gonderilen 28 baytlik telemetri paketlerini cozen yardimci sinif.
Hem Modul 2 (masaustu arayuz) hem de test altyapisi tarafindan kullanilir.

**Sorumluluklar:**
- Bayt akisindan paket basligini (0xAA 0x55) bulma
- Struct unpacking ile alanlari ayristirma
- CRC16 dogrulama
- Hata durumlarini raporlama

### synthetic_data_generator.py
Fiziksel donanim olmadan Modul 2 ve Modul 3 gelistirmesini mumkun kilan sentetik veri ureteci.

**Sorumluluklar:**
- Gercekci sinus dalga tabanlı diz acisi kaliplari uretme
- Yapilandirılabilir gurultu ekleme
- 28 baytlik paket formatinda veri olusturma
- Sanal seri port veya TCP soket uzerinden cikti verme
- Parametreler: frekans, genlik, gurultu seviyesi, cikis portu

## Kullanim

```bash
# Sentetik veri ile masaustu arayuzu test etme
python shared/synthetic_data_generator.py --port COM_VIRTUAL --hz 50 --noise 0.5
```
