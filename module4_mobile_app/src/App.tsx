/**
 * @file App.tsx
 * @brief Mobile Application Entry Point — Dual-Encoder Knee Goniometer
 *
 * Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
 */

import React, { useState } from 'react';
import { StyleSheet, View, Text, TouchableOpacity, SafeAreaView } from 'react-native';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  const [activeTab, setActiveTab] = useState<'dashboard' | 'control' | 'history'>('dashboard');
  const [isConnected, setIsConnected] = useState<boolean>(false);

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="light" />

      {/* Header Bar */}
      <View style={styles.header}>
        <Text style={styles.title}>Knee Goniometer</Text>
        <View style={[styles.statusBadge, isConnected ? styles.connected : styles.disconnected]}>
          <Text style={styles.statusText}>{isConnected ? 'CONNECTED' : 'DISCONNECTED'}</Text>
        </View>
      </View>

      {/* Main Content Area */}
      <View style={styles.content}>
        {activeTab === 'dashboard' && (
          <View style={styles.placeholderContainer}>
            <Text style={styles.placeholderText}>[DashboardScreen: Live Angular Gauge & Telemetry Curves]</Text>
          </View>
        )}
        {activeTab === 'control' && (
          <View style={styles.placeholderContainer}>
            <Text style={styles.placeholderText}>[ControlScreen: Z/S/P Calibration & Recording Dispatcher]</Text>
          </View>
        )}
        {activeTab === 'history' && (
          <View style={styles.placeholderContainer}>
            <Text style={styles.placeholderText}>[HistoryScreen: Cached Session Records & CSV Export]</Text>
          </View>
        )}
      </View>

      {/* Bottom Navigation Bar */}
      <View style={styles.tabBar}>
        <TouchableOpacity
          style={[styles.tabButton, activeTab === 'dashboard' && styles.activeTab]}
          onPress={() => setActiveTab('dashboard')}
        >
          <Text style={styles.tabText}>Dashboard</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tabButton, activeTab === 'control' && styles.activeTab]}
          onPress={() => setActiveTab('control')}
        >
          <Text style={styles.tabText}>Control</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tabButton, activeTab === 'history' && styles.activeTab]}
          onPress={() => setActiveTab('history')}
        >
          <Text style={styles.tabText}>History</Text>
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
    fontSize: 11,
    fontWeight: '700',
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
