/**
 * @file DashboardScreen.tsx
 * @brief Live Angular Waveform & Dial Gauge Dashboard Screen
 *
 * Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
 */

import React, { useState } from 'react';
import { StyleSheet, View, Text, ScrollView } from 'react-native';

export const DashboardScreen: React.FC = () => {
  const [leftAngle, setLeftAngle] = useState<number>(0.0);
  const [rightAngle, setRightAngle] = useState<number>(0.0);
  const [packetRate, setPacketRate] = useState<number>(50);

  return (
    <ScrollView style={styles.container}>
      {/* Top Metric Cards */}
      <View style={styles.metricsRow}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>LEFT KNEE</Text>
          <Text style={styles.angleValue}>{leftAngle.toFixed(1)}°</Text>
          <Text style={styles.cardSubtitle}>Encoder Flexion</Text>
        </View>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>RIGHT KNEE</Text>
          <Text style={styles.angleValue}>{rightAngle.toFixed(1)}°</Text>
          <Text style={styles.cardSubtitle}>Encoder Flexion</Text>
        </View>
      </View>

      {/* Semicircular Dynamic Gauge Container */}
      <View style={styles.gaugeContainer}>
        <Text style={styles.gaugeHeader}>Real-Time Angular Gauge (0° - 150°)</Text>
        <View style={styles.gaugeMock}>
          <Text style={styles.mockText}>[AngleGauge SVG Dial: {leftAngle.toFixed(1)}°]</Text>
        </View>
      </View>

      {/* Stream Diagnostics Footer */}
      <View style={styles.footerInfo}>
        <Text style={styles.infoText}>Stream Rate: {packetRate} Hz (Nominal: 50 Hz)</Text>
        <Text style={styles.infoText}>Packet Loss: 0.0%</Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
  },
  metricsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  card: {
    flex: 0.48,
    backgroundColor: '#1E1E1E',
    borderRadius: 8,
    padding: 16,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#2D2D2D',
  },
  cardTitle: {
    color: '#00B4D8',
    fontSize: 14,
    fontWeight: 'bold',
  },
  angleValue: {
    color: '#FFFFFF',
    fontSize: 32,
    fontWeight: 'bold',
    marginVertical: 8,
  },
  cardSubtitle: {
    color: '#888888',
    fontSize: 12,
  },
  gaugeContainer: {
    backgroundColor: '#1E1E1E',
    borderRadius: 8,
    padding: 16,
    alignItems: 'center',
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#2D2D2D',
  },
  gaugeHeader: {
    color: '#E0E0E0',
    fontSize: 15,
    marginBottom: 12,
  },
  gaugeMock: {
    height: 180,
    width: '100%',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#262626',
    borderRadius: 6,
  },
  mockText: {
    color: '#AAAAAA',
    fontSize: 13,
  },
  footerInfo: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 8,
  },
  infoText: {
    color: '#666666',
    fontSize: 12,
  },
});
