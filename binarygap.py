N=[1,2,3,9,21,12345]

def solution(n):
    # write your code in Python 3.6
    
    ou = bin(n)[2:].strip('0').strip('1').split('1')
    print(max(ou))
    #len(max(bin(N)[2:].strip('0').strip('1').split('1')))
    

for mm in N:
    solution(mm)

print("")