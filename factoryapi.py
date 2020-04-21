#factoryapi ArTV

# Message: E0 LEN COMID DEVICEID REGIONID ADDRESSHIGH ADDRESSLOW DATALEN DATA0 DATA1 … CRC 
# [starter Len read/write devID regID Register LowAdress Byte DATA CRC]

#E0 0A 5F 02 01 00 08 01 AB FF

starter = ["E0"]
length=["0A"]
writeDev=["5F"]
devID=["02"]
regionID=["01"]
registerHigh=["00"]
registerLow = ["08"]
bytelen=["01"]
data=["AA"]

total = starter + length + writeDev + devID + regionID + registerHigh + registerLow + bytelen + data

print(total)


out = [int(x, 16) for x in total]
print (out)

sum = int("FF",16)

for x in out:
    sum= (sum - x) %256

sum_hex = hex(sum)

print(f"CRC:{sum} | {sum_hex}")

sum_hex=[sum_hex[-2]+sum_hex[-1]] #only get last 2 character.. 
total += sum_hex

print(f"new frame: {total}")

#print(int(starter, 16))
