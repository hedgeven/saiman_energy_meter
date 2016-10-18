#!/usr/bin/env python3

import sys
import time
import serial
import minimalmodbus

SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_SPEED = 9600
SERIAL_TIMEOUT = 0.5
SERIAL_PARITY = serial.PARITY_NONE
MODBUS_DEBUG = False

class SaimanEnergyMeter:
    """A simple class for Saiman Energy Meters (Дала СА4-Э720 П RS)"""

    def __init__(self,
                 address,
                 serial_port=SERIAL_PORT,
                 serial_speed=SERIAL_SPEED,
                 serial_timeout=SERIAL_TIMEOUT,
                 serial_parity=SERIAL_PARITY,
                 debug=MODBUS_DEBUG):
        self.address = address
        self.serial_port = serial_port
        self.serial_speed = serial_speed
        self.serial_timeout = serial_timeout
        self.serial_parity = serial_parity
        self.debug = debug

        self.configure()
        self.conn_open()
        self.count_energy()
        self.conn_close()
   
    def configure(self):
        try:
            self.instrument = minimalmodbus.Instrument(self.serial_port, self.address)
            self.instrument.serial.baudrate = self.serial_speed
            self.instrument.serial.timeout = self.serial_timeout
            self.instrument.serial.parity = self.serial_parity
            self.instrument.debug = self.debug
        except Exception as e:
            print(e)
            sys.exit(1)

    def conn_open(self):
        try:
            #self.instrument._performCommand(0x8, '\x00\x00\x00\x00')
            #self.instrument._performCommand(0x44, '')
            self.instrument._performCommand(0x41, '\x01\x31\x31\x31\x31\x31\x31')
            time.sleep(self.serial_timeout)
        except Exception as e:
            print(e)
            sys.exit(1)

    def conn_close(self):
        try:
            self.instrument._performCommand(0x42, '')
            time.sleep(self.serial_timeout)
        except:
            pass

    def get_reg(self, payload):
        try:
            time.sleep(self.serial_timeout)
            return self.instrument._performCommand(0x3, payload)
        except:
            return 0

    def count_energy(self):
        self.reg1 = self.get_reg('\x01\x20\x00\x0E')
        self.reg2 = self.get_reg('\x0D\xA0\x00\x0E')
        if self.reg1 == 0 and self.reg2 == 0:
           print("No data")
           sys.exit(1)
        elif self.reg1 == 0:
           self.reg1 = self.reg2
        elif self.reg2 == 0:
           self.reg2 = self.reg1
        self.t1 = ( int(''.join(minimalmodbus._hexlify(self.reg1).split(' ')[1:6][::-1])) +
               int(''.join(minimalmodbus._hexlify(self.reg2).split(' ')[1:6][::-1])) )/100
        self.t2 = ( int(''.join(minimalmodbus._hexlify(self.reg1).split(' ')[6:11][::-1])) +
               int(''.join(minimalmodbus._hexlify(self.reg2).split(' ')[6:11][::-1])) )/100
        self.t3 = ( int(''.join(minimalmodbus._hexlify(self.reg1).split(' ')[11:16][::-1])) +
               int(''.join(minimalmodbus._hexlify(self.reg2).split(' ')[11:16][::-1])) )/100
        self.total_energy = self.t1 + self.t2 + self.t3
