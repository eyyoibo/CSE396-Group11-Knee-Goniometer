/**
 * @file BluetoothService.ts
 * @brief Bluetooth Classic SPP & BLE Service Management
 *
 * Project Team: Ibrahim Halil Dogan, Mert Canoglu, Cem Baygin, Cansu Bulut
 */

export interface TelemetryData {
  sequenceNumber: number;
  timestampMs: number;
  leftCount: number;
  rightCount: number;
  leftAngle: number;
  rightAngle: number;
}

export type ConnectionState = 'DISCONNECTED' | 'SCANNING' | 'CONNECTING' | 'CONNECTED';

export class BluetoothService {
  private static instance: BluetoothService;
  private state: ConnectionState = 'DISCONNECTED';
  private targetDeviceAddress: string | null = null;

  private constructor() {}

  public static getInstance(): BluetoothService {
    if (!BluetoothService.instance) {
      BluetoothService.instance = new BluetoothService();
    }
    return BluetoothService.instance;
  }

  /**
   * Scans for nearby Bluetooth devices advertising SPP services.
   */
  public async scanDevices(): Promise<any[]> {
    // TODO: Request runtime permissions (BLUETOOTH_SCAN, ACCESS_FINE_LOCATION)
    // TODO: Call react-native-bluetooth-classic.startDiscovery()
    throw new Error('scanDevices() not yet implemented.');
  }

  /**
   * Establishes RFCOMM socket connection with selected ESP32 device.
   */
  public async connect(deviceAddress: string): Promise<boolean> {
    // TODO: Open SPP socket to deviceAddress
    // TODO: On success, begin reading continuous byte stream
    throw new Error('connect() not yet implemented.');
  }

  /**
   * Terminates active Bluetooth session.
   */
  public async disconnect(): Promise<void> {
    // TODO: Close socket handle safely
    throw new Error('disconnect() not yet implemented.');
  }

  /**
   * Transmits single-byte ASCII command to hardware ('Z', 'S', 'P').
   */
  public async sendCommand(command: 'Z' | 'S' | 'P'): Promise<void> {
    // TODO: Write ASCII string `${command}\n` to open socket
    throw new Error('sendCommand() not yet implemented.');
  }

  /**
   * Unpacks 28-byte binary frame into TelemetryData object.
   */
  public parsePacket(buffer: Uint8Array): TelemetryData | null {
    // TODO: Validate header [0xAA, 0x55] and CRC-16 checksum
    // TODO: Unpack little-endian fields into TelemetryData
    throw new Error('parsePacket() not yet implemented.');
  }

  /**
   * Subscribes a listener callback to validated telemetry frames.
   */
  public onDataReceived(callback: (data: TelemetryData) => void): () => void {
    // TODO: Register subscriber and return unsubscribe closure
    return () => {};
  }
}
