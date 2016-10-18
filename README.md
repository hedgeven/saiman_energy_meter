# saiman_energy_meter
A simple library for getting data Saiman Energy Meters (Дала СА4-Э720 П RS)

## Usage:
* Clone this repo

<!-- language: bash -->

    git clone https://github.com/hedgeven/saiman_energy_meter.git
    
* Get minimalmodbus library

<!-- language: bash -->

    wget https://raw.githubusercontent.com/pyhys/minimalmodbus/master/minimalmodbus.py

* Modify one string in minimalmodbus library

<!-- language: bash -->

    sed -i 's/return _numToTwoByteString(register, LsbFirst=True)/return _numToTwoByteString(register, LsbFirst=False)/g' minimalmodbus.py

* Run find_devices.py with correct serial port

<!-- language: bash -->
    python3 ./find_devices.py /dev/ttyUSB0
