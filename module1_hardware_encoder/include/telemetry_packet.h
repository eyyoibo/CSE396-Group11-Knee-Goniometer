/**
 * @file telemetry_packet.h
 * @brief Diz Gonyometresi - Telemetri Paket Tanımları ve Sabitler
 *
 * 28 baytlık ikili paket yapısı, komut/durum numaralandırmaları
 * ve ilgili sabitlerin tanımlarını içerir.
 *
 * Proje Ekibi: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
 * Danışman: Prof. Dr. Erkan Zergeroglu
 */

#ifndef TELEMETRY_PACKET_H
#define TELEMETRY_PACKET_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ===================== Sabitler ===================== */

/** Paket başlık baytları */
#define PACKET_HEADER_0         0xAA
#define PACKET_HEADER_1         0x55

/** Enkoder parametreleri */
#define ENCODER_PPR             5000        /* Devir başına darbe sayısı        */
#define QUADRATURE_MULTIPLIER   4           /* 4x kuadratür çözme çarpanı       */
#define COUNTS_PER_REV          (ENCODER_PPR * QUADRATURE_MULTIPLIER)  /* 20000 */
#define DEG_PER_COUNT           (360.0f / (float)COUNTS_PER_REV)       /* 0.018 */

/** Telemetri gönderim frekansı */
#define TX_FREQ_HZ              50          /* Saniyede gönderilecek paket      */
#define TX_PERIOD_MS            (1000 / TX_FREQ_HZ)                    /* 20 ms */

/** Paket boyutu (bayt) */
#define PACKET_SIZE             28

/* ===================== Komut Tanımları ===================== */

/**
 * @brief Masaüstü uygulamasından gelebilecek komutlar.
 *
 * Tek baytlık ASCII karakterleri olarak Bluetooth SPP üzerinden alınır.
 */
typedef enum {
    CMD_ZERO    = 'Z',   /**< Enkoder sayaçlarını sıfırla (kalibrasyon)  */
    CMD_START   = 'S',   /**< Telemetri akışını başlat                   */
    CMD_PAUSE   = 'P'    /**< Telemetri akışını duraklat                 */
} command_t;

/* ===================== Cihaz Durum Tanımları ===================== */

/**
 * @brief Cihazın çalışma durumlarını tanımlar.
 */
typedef enum {
    STATE_IDLE,          /**< Boşta — veri gönderilmiyor                */
    STATE_STREAMING,     /**< Aktif — 50 Hz telemetri akışı yapılıyor   */
    STATE_CALIBRATING    /**< Kalibrasyon — sayaçlar sıfırlanıyor       */
} device_state_t;

/* ===================== Paket Yapısı ===================== */

/**
 * @brief 28 baytlık telemetri paketi.
 *
 * Bellek hizalamasını önlemek için packed özniteliği kullanılır;
 * böylece yapı tam olarak 28 bayt tutar.
 *
 * Alan düzeni:
 *   [0-1]    header       0xAA 0x55
 *   [2-5]    seq          Artan sıra numarası
 *   [6-9]    timestamp_ms Başlangıçtan itibaren milisaniye
 *   [10-13]  left_count   Sol enkoder ham sayım
 *   [14-17]  right_count  Sağ enkoder ham sayım
 *   [18-21]  left_angle   Sol diz açısı (derece)
 *   [22-25]  right_angle  Sağ diz açısı (derece)
 *   [26-27]  crc16        CRC-16/CCITT kontrol toplamı
 */
typedef struct __attribute__((packed)) {
    uint8_t  header[2];       /**< Sabit başlık: {0xAA, 0x55}           */
    uint32_t seq;             /**< Paket sıra numarası                  */
    uint32_t timestamp_ms;    /**< Zaman damgası (ms)                   */
    int32_t  left_count;      /**< Sol enkoder ham sayım değeri         */
    int32_t  right_count;     /**< Sağ enkoder ham sayım değeri         */
    float    left_angle;      /**< Sol diz açısı (derece)               */
    float    right_angle;     /**< Sağ diz açısı (derece)               */
    uint16_t crc16;           /**< CRC-16/CCITT kontrol toplamı         */
} telemetry_packet_t;

/* Derleme zamanı boyut kontrolü */
_Static_assert(sizeof(telemetry_packet_t) == PACKET_SIZE,
               "Paket boyutu 28 bayt olmali!");

/* ===================== Fonksiyon Prototipleri ===================== */

/**
 * @brief PCNT birimlerini her iki enkoder için yapılandırır.
 */
void pcnt_init_encoders(void);

/**
 * @brief Ham sayım değerinden açı hesaplar.
 * @param counts  PCNT ham sayım değeri
 * @return        Derece cinsinden açı
 */
float calculate_angle_from_counts(int32_t counts);

/**
 * @brief Bluetooth Classic SPP sunucusunu başlatır.
 */
void bluetooth_spp_init(void);

/**
 * @brief Telemetri paketini SPP üzerinden gönderir.
 * @param pkt  Gönderilecek paket
 */
void send_telemetry_packet(const telemetry_packet_t *pkt);

/**
 * @brief Alınan komutu işler ve durum geçişi yapar.
 * @param cmd  Alınan komut baytı
 */
void handle_command(uint8_t cmd);

/**
 * @brief Telemetri paketini verilen parametrelerle oluşturur.
 * @param pkt          Doldurulacak paket
 * @param seq          Sıra numarası
 * @param left_count   Sol enkoder sayımı
 * @param right_count  Sağ enkoder sayımı
 */
void build_packet(telemetry_packet_t *pkt, uint32_t seq,
                  int32_t left_count, int32_t right_count);

/**
 * @brief Verilen veri üzerinde CRC-16/CCITT hesaplar.
 * @param data    Veri tampon adresi
 * @param length  Veri uzunluğu (bayt)
 * @return        16-bit CRC değeri
 */
uint16_t compute_crc16(const uint8_t *data, size_t length);

#ifdef __cplusplus
}
#endif

#endif /* TELEMETRY_PACKET_H */
