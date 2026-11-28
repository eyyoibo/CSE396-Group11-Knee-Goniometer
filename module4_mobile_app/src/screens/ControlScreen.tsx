/**
 * @file ControlScreen.tsx
 * @brief Remote Z/S/P Hardware Calibration & Session Control Screen
 *
 * Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
 */

import React, { useState } from 'react';
import { StyleSheet, View, Text, TouchableOpacity, Alert } from 'react-native';

export const ControlScreen: React.FC = () => {
  const [sessionActive, setSessionActive] = useState<boolean>(false);

  const handleZeroCalibration = () => {
    Alert.alert(
      'Zero Calibration (Z)',
      'Is the participant standing in full neutral extension? Current encoder counts will be set as 0.0° baseline.',
      [
        { text: 'Cancel', style: 'cancel' },
        { 
          text: 'Calibrate', 
          onPress: () => {
            // TODO: BluetoothService.getInstance().sendCommand('Z');
            console.log("Transmitted command: 'Z'");
          } 
        }
      ]
    );
  };

  const handleStartSession = () => {
    // TODO: BluetoothService.getInstance().sendCommand('S');
    setSessionActive(true);
    console.log("Transmitted command: 'S'");
  };

  const handlePauseSession = () => {
    // TODO: BluetoothService.getInstance().sendCommand('P');
    setSessionActive(false);
    console.log("Transmitted command: 'P'");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Remote ESP32 Hardware Controls</Text>

      {/* Zero Calibration Button */}
      <TouchableOpacity 
        style={[styles.btn, styles.zeroBtn]}
        onPress={handleZeroCalibration}
      >
        <Text style={styles.btnText}>[Z] ZERO CALIBRATION</Text>
        <Text style={styles.btnSub}>Calibrate current posture as 0.0°</Text>
      </TouchableOpacity>

      {/* Start Session Button */}
      <TouchableOpacity 
        style={[styles.btn, styles.startBtn, sessionActive && styles.disabledBtn]}
        onPress={handleStartSession}
        disabled={sessionActive}
      >
        <Text style={styles.btnText}>[S] START STREAMING</Text>
        <Text style={styles.btnSub}>Begin 50 Hz telemetry transmission</Text>
      </TouchableOpacity>

      {/* Pause Session Button */}
      <TouchableOpacity 
        style={[styles.btn, styles.pauseBtn, !sessionActive && styles.disabledBtn]}
        onPress={handlePauseSession}
        disabled={!sessionActive}
      >
        <Text style={styles.btnText}>[P] PAUSE STREAMING</Text>
        <Text style={styles.btnSub}>Halt telemetry transmission</Text>
      </TouchableOpacity>

      {/* Active State Banner */}
      <View style={styles.statusBox}>
        <Text style={styles.statusLabel}>Session Status:</Text>
        <Text style={[styles.statusValue, sessionActive ? styles.activeText : styles.inactiveText]}>
          {sessionActive ? 'STREAMING ACTIVE (50 Hz)' : 'IDLE / PAUSED'}
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
