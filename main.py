
import modulesPA as mp
import myvars as mv

print("-\n--\n---\n----\n-----\n------")

from pymodbus.client.sync import ModbusTcpClient

for idx, ipAdrs in enumerate(mv.ipAddressList):
    client = ModbusTcpClient(ipAdrs)
    client.connect()
    # registers are addressed starting from zero
    result = client.read_holding_registers(2699, 2, unit=0x00)
    print(result.registers)

print("---\n--\n-")