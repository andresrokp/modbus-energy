
import modulesPA as mp
import myvars as mv
import datetime
import openpyxl

print("-\n--\n---\n----\n-----\n------")

# iterate over the devices wich are defined in list at myvars.py file
for idx, ipAdrs in enumerate(mv.ipAddressList):
    ip = ipAdrs[0]
    name =  ipAdrs[1]
    print(ip, "\n", name)
    try:
        rawDataFloat32 = mp.queryMP(ip)
        energyValue = mp.conv754toDEC(*rawDataFloat32)
        mp.consolePrint(rawDataFloat32, energyValue)
    except(Exception) as e:
        mp.errorPrint(e)
    

dateAndTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print("\n", "MOMENTO DE CAPTURA: ", dateAndTime)
print("---\n--\n-")