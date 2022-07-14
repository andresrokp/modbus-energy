
import modulesPA as mp
import myvars as mv
import datetime

print("-\n--\n---\n----\n-----\n------")

# iterate over the devices wich are defined in list at myvars.py file
for idx, ipAdrs in enumerate(mv.ipAddressList):
    ip = ipAdrs[0]
    name =  ipAdrs[1]
    print(ip, "\n", name)
    try:
        # ToDo : guarantie the rigth unit in holding read to succes in ion9000 and pm5000
        rawDataFloat32 = mp.queryMP(ip)
        energyValue = mp.conv754toDEC(*rawDataFloat32)
        print("",rawDataFloat32)
        print(" Pot Activa Acum:  ", energyValue,"kWh")
        print("-")
    except(Exception) as e:
        print(" :(  Error, :: ", e)
        print("-")
    

dateAndTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print("\n", "MOMENTO DE CAPTURA: ", dateAndTime)
print("---\n--\n-")