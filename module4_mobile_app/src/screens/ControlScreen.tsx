/**
 * @file ControlScreen.tsx
 * @brief Uzaktan Z/S/P Kalibrasyon ve Seans Kontrol Ekrani
 *
 * Proje Ekibi: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
 * Akademik Danisman: Prof. Dr. Erkan Zergeroglu
 */

import React, { useState } from 'react';
import { StyleSheet, View, Text, TouchableOpacity, Alert } from 'react-native';

// import { BluetoothService } from '../services/BluetoothService';

export const ControlScreen: React.FC = () => {
  const [sessionActive, setSessionActive] = useState<boolean>(false);
  const [elapsedSeconds, setElapsedSeconds] = useState<number>(0);

  const handleZeroCalibration = () => {
    Alert.alert(
      'Sifir Kalibrasyonu (Z)',
      'Katilimcinin bacaklari duz konumda mi? Mevcut enkoder sayaci 0 derece referansi olarak ayarlanacaktir.',
      [
        { text: 'Iptal', style: 'cancel' },
        { 
          text: 'Sifirla', 
          onPress: () => {
            // TODO: BluetoothService.getInstance().sendCommand('Z');
            console.log("Komut gonderildi: Z");
          } 
        }
      ]
    );
  };

  const handleStartSession = () => {
    // TODO: BluetoothService.getInstance().sendCommand('S');
    setSessionActive(true);
    console.log("Komut gonderildi: S");
  };

  const handlePauseSession = () => {
    // TODO: BluetoothService.getInstance().sendCommand('P');
    setSessionActive(false);
    console.log("Komut gonderildi: P");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Uzaktan ESP32 Komut Kontrolu</Text>

      {/* Sifir Kalibrasyon Butonu */}
      <TouchableOpacity 
        style={[styles.btn, styles.zeroBtn]}
        onPress={handleZeroCalibration}
      >
        <Text style={styles.btnText}>[Z] SIFIR KALIBRASYONU</Text>
        <Text style={styles.btnSub}>Mevcut durusu 0° referansi yap</Text>
      </TouchableOpacity>

      {/* Baslat Butonu */}
      <TouchableOpacity 
        style={[styles.btn, styles.startBtn, sessionActive && styles.disabledBtn]}
        onPress={handleStartSession}
        disabled={sessionActive}
      >
        <Text style={styles.btnText}>[S] OLCUMU BASLAT</Text>
        <Text style={styles.btnSub}>50 Hz telemetri akisini baslat</Text>
      </TouchableOpacity>

      {/* Durdur Butonu */}
      <TouchableOpacity 
        style={[styles.btn, styles.pauseBtn, !sessionActive && styles.disabledBtn]}
        onPress={handlePauseSession}
        disabled={!sessionActive}
      >
        <Text style={styles.btnText}>[P] OLCUMU DURAKLAT</Text>
        <Text style={styles.btnSub}>Paket iletimini dondur</Text>
      </TouchableOpacity>

      {/* Oturum Durumu */}
      <View style={styles.statusBox}>
        <Text style={styles.statusLabel}>Oturum Durumu:</Text>
        <Text style={[styles.statusValue, sessionActive ? styles.activeText : styles.inactiveText]}>
          {sessionActive ? 'KAYIT AKTIF (50 Hz)' : 'BEKLEMEDE'}
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
    padding: 16,
  },
  title: {
    color: '#E0E0E0',
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  btn: {
    borderRadius: 8,
    padding: 18,
    alignItems: 'center',
    marginBottom: 16,
  },
  zeroBtn: {
    backgroundColor: '#E65100',
  },
  startBtn: {
    backgroundColor: '#2E7D32',
  },
  pauseBtn: {
    backgroundColor: '#C62828',
  },
  disabledBtn: {
    opacity: 0.4,
  },
  btnText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
  btnSub: {
    color: '#EEEEEE',
    fontSize: 12,
    marginTop: 4,
  },
  statusBox: {
    marginTop: 24,
    padding: 16,
    backgroundColor: '#1E1E1E',
    borderRadius: 8,
    alignItems: 'center',
  },
  statusLabel: {
    color: '#888888',
    fontSize: 13,
  },
  statusValue: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 6,
  },
  activeText: {
    color: '#4CAF50',
  },
  inactiveText: {
    color: '#B0BEC5',
  },
});
