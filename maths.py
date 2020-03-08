# lets do some maths... use lots of functions/methods....

numList=[1,2,3,4,5,5,6,78,8,9,0]
print(min(numList), max(numList))

mixList = [1,2,'12', 'OTTO', 0x56]
try:
    print(min(mixList), max(mixList))
except Exception as e:
    print("does not support compare int - str etc... ")
