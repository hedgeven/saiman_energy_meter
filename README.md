# saiman_energy_meter
A simple library for getting data Saiman Energy Meters (Дала СА4-Э720 П RS)

## Usage:
* Clone this repo
* Get minimalmodbus library
wget https://raw.githubusercontent.com/pyhys/minimalmodbus/master/minimalmodbus.py
* Modify one string in minimalmodbus library
sed -i 's/return _numToTwoByteString(register, LsbFirst=True)/return _numToTwoByteString(register, LsbFirst=False)/g' minimalmodbus.py
* Run find_devices.py
