
import modulesPA as mp
import myvars as mv
import datetime

print("-\n--\n---\n----\n-----\n------")

from pymodbus.client.sync import ModbusTcpClient

for idx, ipAdrs in enumerate(mv.ipAddressList):
    client = ModbusTcpClient(ipAdrs)
    client.connect()
    # registers are addressed starting from zero
    result = client.read_holding_registers(2699, 2, unit=0x00)
    energyValue = mp.conv754toDEC(*result.registers)
    print(ipAdrs, "\n", mv.placeNameList[idx])
    print("",result.registers)
    print(" Pot Activa Acum:  ", energyValue,"kWh")
    print("-")
    client.close()

dateAndTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print("\n", "MOMENTO DE CAPTURA: ", dateAndTime)
print("---\n--\n-")