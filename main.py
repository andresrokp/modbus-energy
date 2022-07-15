
import modulesPM as mp
import myvars as mv
import datetime

print("-\n--\n---\n----")

dataLogger = []

# iterate over the devices wich are defined in list at myvars.py file
for idx, ipAdrs in enumerate(mv.ipAddressList[1:14]):
    ip, name = mp.pickAddress(ipAdrs)
    try:
        result = mp.queryPmData(ip)
    except(Exception) as e:
        result = e
    mp.consolePrint(result, ip, name)
    dataLogger.append([name, ip, result if type(result) == float else str(result)])
    
mp.xlxsPrint(dataLogger)
    
dateAndTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("\nMOMENTO DE CAPTURA: ", dateAndTime)
print(dataLogger)
print("----\n---\n--\n-")