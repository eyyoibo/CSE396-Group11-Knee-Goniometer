/**
 * @file AngleGauge.tsx
 * @brief Analog Kadran (Gauge) Bileseni Iskeleti
 *
 * Proje Ekibi: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
 * Akademik Danisman: Prof. Dr. Erkan Zergeroglu
 */

import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

interface AngleGaugeProps {
  angle: number;           // 0° - 150°
  minAngle?: number;       // Varsayilan 0
  maxAngle?: number;       // Varsayilan 150
  size?: number;           // Genislik/Yukseklik
  label?: string;          // Ornek: "Sol Bacak"
}

export const AngleGauge: React.FC<AngleGaugeProps> = ({
  angle,
  minAngle = 0,
  maxAngle = 150,
  size = 220,
  label = 'Diz Fleksiyon Acisi',
}) => {
  // TODO: react-native-svg kullanarak yarim dairesel yay ciz
  // TODO: Aci degerine gore ibre (needle) rotasyon acisini hesapla:
  //       const rotationDeg = ((angle - minAngle) / (maxAngle - minAngle)) * 180 - 90;
  // TODO: Guvenli hareket bolgesi (0-30 kirmizi, 30-120 yesil, 120+ sari) renk segmentlerini ciz

  return (
    <View style={[styles.container, { width: size, height: size * 0.7 }]}>
      <Text style={styles.label}>{label}</Text>
      <View style={styles.gaugePlaceholder}>
        <Text style={styles.angleDisplay}>{angle.toFixed(1)}°</Text>
        <Text style={styles.rangeText}>{minAngle}° - {maxAngle}°</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#1E1E1E',
    borderRadius: 8,
    padding: 12,
  },
  label: {
    color: '#888888',
    fontSize: 13,
    marginBottom: 8,
  },
  gaugePlaceholder: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  angleDisplay: {
    color: '#00B4D8',
    fontSize: 28,
    fontWeight: 'bold',
  },
  rangeText: {
    color: '#666666',
    fontSize: 11,
    marginTop: 4,
  },
});
