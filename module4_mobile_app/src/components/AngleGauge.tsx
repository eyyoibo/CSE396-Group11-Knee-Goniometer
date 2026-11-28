/**
 * @file AngleGauge.tsx
 * @brief Dynamic Semicircular Angular Dial Component
 *
 * Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
 */

import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

interface AngleGaugeProps {
  angle: number;           // 0° to 150°
  minAngle?: number;       // Default: 0
  maxAngle?: number;       // Default: 150
  size?: number;           // Width/height dimension
  label?: string;          // e.g. "Left Knee Flexion"
}

export const AngleGauge: React.FC<AngleGaugeProps> = ({
  angle,
  minAngle = 0,
  maxAngle = 150,
  size = 220,
  label = 'Knee Flexion Angle',
}) => {
  return (
    <View style={[styles.container, { width: size, height: size * 0.7 }]}>
      <Text style={styles.label}>{label}</Text>
      <View style={styles.gaugePlaceholder}>
        <Text style={styles.angleDisplay}>{angle.toFixed(1)}°</Text>
        <Text style={styles.rangeText}>{minAngle}° – {maxAngle}°</Text>
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
