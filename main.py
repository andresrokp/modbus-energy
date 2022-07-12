
import modulesPA as mp
import myvars as mv
import datetime

print("-\n--\n---\n----\n-----\n------")

# iterate over the devices wich are defined in list at myvars.py file
for idx, ipAdrs in enumerate(mv.ipAddressList):
    rawDataFloat32 = mp.queryMP(ipAdrs)
    energyValue = mp.conv754toDEC(*rawDataFloat32)
    print(ipAdrs, "\n", mv.placeNameList[idx])
    print("",rawDataFloat32)
    print(" Pot Activa Acum:  ", energyValue,"kWh")
    print("-")
    

dateAndTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print("\n", "MOMENTO DE CAPTURA: ", dateAndTime)
print("---\n--\n-")