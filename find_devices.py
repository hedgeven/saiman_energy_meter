#!/usr/bin/env python3

import sys
from saiman_energy_meter import SaimanEnergyMeter

def main(argv):

    if len(argv) < 2:
        print("Please, specify serial port. Example: %s /dev/ttyUSB0" % argv[0])
        sys.exit(1)

    serial_port = argv[1]
    for addr in range(1,248):
        try:
            print('%d - ' % addr, end="")
            if SaimanEnergyMeter(addr, serial_port):
                print("Ok")
        except:
             pass

if __name__ == "__main__":
    main(sys.argv)
