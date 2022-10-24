
print("-\n--\n---\n----")
from pymodbus.client.sync import ModbusTcpClient

ip = "192.168.25.19";
client = ModbusTcpClient(ip);
reading = client.read_holding_registers(3203,4,unit=0x00)
client.close()
print(reading.registers)

print("-\n--\n---\n----")