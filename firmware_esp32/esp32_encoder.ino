/*
 * =====================================================================================
 * CSE 396 - Computer Engineering Project
 * Group 11: Wireless Wearable Dual-Encoder Knee Goniometer
 * Module 1: Mechanical & Wireless ESP32 Hardware Firmware
 *
 * Description:
 *   Quadrature decoding for two incremental rotary encoders mounted on a
 *   polycentric knee brace using ESP32 hardware interrupts.
 *   Streams calibrated knee angle & raw pulse counts wirelessly over Bluetooth Serial (SPP)
 *   at 50 Hz (20ms interval).
 *
 * Advisor: Prof. Dr. Erkan Zergeroğlu
 * Authors: İbrahim Halil Doğan, Mert Canoğlu, Cem Baygın, Cansu Bulut
 * =====================================================================================
 */

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to enable it
#endif

BluetoothSerial SerialBT;

// --- Pin Definitions for Dual Rotary Encoders ---
// Encoder 1 (Femur / Upper Limb)
const int ENC1_PIN_A = 18;
const int ENC1_PIN_B = 19;

// Encoder 2 (Tibia / Lower Limb)
const int ENC2_PIN_A = 22;
const int ENC2_PIN_B = 23;

// --- Calibration Constants ---
const float ENCODER_PPR = 600.0f; // Pulses Per Revolution
const float K1 = 360.0f / ENCODER_PPR;
const float K2 = 360.0f / ENCODER_PPR;

// --- Volatile Pulse Counters (Modified in ISR) ---
volatile long encoder1_pulses = 0;
volatile long encoder2_pulses = 0;

// --- Timing ---
unsigned long last_transmit_time = 0;
const unsigned long TRANSMIT_INTERVAL_MS = 20; // 50 Hz streaming rate

// --- Interrupt Service Routines (ISRs) ---
void IRAM_ATTR isr_encoder1() {
  int stateB = digitalRead(ENC1_PIN_B);
  if (stateB > 0) {
    encoder1_pulses++;
  } else {
    encoder1_pulses--;
  }
}

void IRAM_ATTR isr_encoder2() {
  int stateB = digitalRead(ENC2_PIN_B);
  if (stateB > 0) {
    encoder2_pulses++;
  } else {
    encoder2_pulses--;
  }
}

void setup() {
  Serial.begin(115200);
  SerialBT.begin("KneeGoniometer_Group11"); // Bluetooth Device Name
  Serial.println("ESP32 Dual-Encoder Goniometer Initialized.");
  Serial.println("Pair via Bluetooth: KneeGoniometer_Group11");

  // Configure Encoder Pins with Internal Pull-ups
  pinMode(ENC1_PIN_A, INPUT_PULLUP);
  pinMode(ENC1_PIN_B, INPUT_PULLUP);
  pinMode(ENC2_PIN_A, INPUT_PULLUP);
  pinMode(ENC2_PIN_B, INPUT_PULLUP);

  // Attach Interrupts on Phase A Rising Edge
  attachInterrupt(digitalPinToInterrupt(ENC1_PIN_A), isr_encoder1, RISING);
  attachInterrupt(digitalPinToInterrupt(ENC2_PIN_A), isr_encoder2, RISING);
}

void loop() {
  // Listen for Zero Calibration command from PC over Bluetooth Serial
  if (SerialBT.available()) {
    char cmd = SerialBT.read();
    if (cmd == 'Z' || cmd == 'z') {
      noInterrupts();
      encoder1_pulses = 0;
      encoder2_pulses = 0;
      interrupts();
      Serial.println("[CALIBRATION] Zero-baseline calibrated.");
      SerialBT.println("ACK:ZERO");
    }
  }

  // Periodic Telemetry Streaming at 50 Hz
  unsigned long current_time = millis();
  if (current_time - last_transmit_time >= TRANSMIT_INTERVAL_MS) {
    last_transmit_time = current_time;

    long n1, n2;
    noInterrupts();
    n1 = encoder1_pulses;
    n2 = encoder2_pulses;
    interrupts();

    // Kinematic Superposition for Polycentric Joint:
    // theta = K1 * delta_N1 + K2 * delta_N2
    float knee_angle = (K1 * n1) + (K2 * n2);

    // CSV Telemetry format: timestamp_ms,n1,n2,knee_angle
    String packet = String(current_time) + "," + String(n1) + "," + String(n2) + "," + String(knee_angle, 2);

    Serial.println(packet);
    SerialBT.println(packet);
  }
}
