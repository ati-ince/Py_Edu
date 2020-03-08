# lets do some maths... use lots of functions/methods....

numList=[1,2,3,4,5,5,6,78,8,9,0]
print(min(numList), max(numList))

mixList = [1,2,'12', 'OTTO', 0x56]
try:
    print(min(mixList), max(mixList))
except Exception as e:
    print("does not support compare int - str etc... ")

# also have round(x), abs(x), pow(x,y) we have to use in standard library..

# sorted(x) use almost for everythngs....
list_sort = [1,2,3,4,5,'ali', 'mom', 0x44]
try:
    print(sorted(list_sort))
except Exception as e:
    print("does not support sorted int - str etc... ")

list_sort = ['ali', 'veli', 'M', '1']
print(sorted(list_sort))

#use math module for all mathemaical functions... pretty useful
import math 
print(math.sin(math.pi/2))