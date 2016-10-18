#!/usr/bin/env python3

from saiman_energy_meter import SaimanEnergyMeter

def main():
    for addr in range(1,248):
        try:
            print('%d - ' % addr, end="")
            if SaimanEnergyMeter(addr, '/dev/ttyACM0'):
                print("Ok")
        except:
             pass

if __name__ == "__main__":
    main()
