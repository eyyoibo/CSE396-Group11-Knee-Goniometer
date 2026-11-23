/**
 * @file App.tsx
 * @brief Diz Goniyometresi Mobil Uygulama Ana Giris Noktasi
 *
 * Proje Ekibi: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin
 * Akademik Danisman: Prof. Dr. Erkan Zergeroglu
 */

import React, { useState } from 'react';
import { StyleSheet, View, Text, TouchableOpacity, SafeAreaView } from 'react-native';
import { StatusBar } from 'expo-status-bar';

// TODO: Ekran bilesenlerini import et
// import { DashboardScreen } from './screens/DashboardScreen';
// import { ControlScreen } from './screens/ControlScreen';
// import { BluetoothService } from './services/BluetoothService';

export default function App() {
  const [activeTab, setActiveTab] = useState<'dashboard' | 'control' | 'history'>('dashboard');
  const [isConnected, setIsConnected] = useState<boolean>(false);

  // TODO: BluetoothService baglanti durum dinleyicisini useEffect ile bagla
  // TODO: Gelen 50 Hz telemetri paketlerini global state veya context icine aktar

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="light" />
      
      {/* Baslik ve Baglanti Durumu */}
      <View style={styles.header}>
        <Text style={styles.title}>Diz Goniyometresi</Text>
        <View style={[styles.statusBadge, isConnected ? styles.connected : styles.disconnected]}>
          <Text style={styles.statusText}>{isConnected ? 'Bagli' : 'Bagli Degil'}</Text>
        </View>
      </View>

      {/* Ekran Icerik Alani */}
      <View style={styles.content}>
        {activeTab === 'dashboard' && (
          <View style={styles.placeholderContainer}>
            <Text style={styles.placeholderText}>[DashboardScreen: Canli Analog Kadran & Aci Grafigi]</Text>
            {/* TODO: <DashboardScreen /> bilesenini yerlestir */}
          </View>
        )}
        {activeTab === 'control' && (
          <View style={styles.placeholderContainer}>
            <Text style={styles.placeholderText}>[ControlScreen: Z/S/P Butonlari & Sifir Kalibrasyonu]</Text>
            {/* TODO: <ControlScreen /> bilesenini yerlestir */}
          </View>
        )}
        {activeTab === 'history' && (
          <View style={styles.placeholderContainer}>
            <Text style={styles.placeholderText}>[HistoryScreen: Gecmis Seans Kayitlari & CSV Paylasma]</Text>
          </View>
        )}
      </View>

      {/* Alt Sekme Navigasyonu */}
      <View style={styles.tabBar}>
        <TouchableOpacity 
          style={[styles.tabButton, activeTab === 'dashboard' && styles.activeTab]}
          onPress={() => setActiveTab('dashboard')}
        >
          <Text style={styles.tabText}>Gosterge</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          style={[styles.tabButton, activeTab === 'control' && styles.activeTab]}
          onPress={() => setActiveTab('control')}
        >
          <Text style={styles.tabText}>Kontrol</Text>
        </TouchableOpacity>
        <TouchableOpacity 
          style={[styles.tabButton, activeTab === 'history' && styles.activeTab]}
          onPress={() => setActiveTab('history')}
        >
          <Text style={styles.tabText}>Gecmis</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#262626',
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  statusBadge: {
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  connected: {
    backgroundColor: '#2E7D32',
  },
  disconnected: {
    backgroundColor: '#C62828',
  },
  statusText: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: '600',
  },
  content: {
    flex: 1,
    padding: 16,
  },
  placeholderContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  placeholderText: {
    color: '#888888',
    textAlign: 'center',
    fontSize: 14,
  },
  tabBar: {
    flexDirection: 'row',
    height: 56,
    borderTopWidth: 1,
    borderTopColor: '#262626',
    backgroundColor: '#1E1E1E',
  },
  tabButton: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  activeTab: {
    borderTopWidth: 2,
    borderTopColor: '#00B4D8',
  },
  tabText: {
    color: '#E0E0E0',
    fontSize: 13,
  },
});
