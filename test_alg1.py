def inp(states,days):
    buf = [0] + states + [0] ;  print(len(buf),buf)
    out=[0]*10; print(len(out),out)
    for d,x in enumerate(range(days)):
        print("buf:",buf)
        for i,y in enumerate(range(1,len(states)+1)):
            if buf[i-1]==buf[i+1]:
                print(f"{y}:1st->",buf[i-1],1,buf[i+1])
                out[i]=0
            else:
                out[i]=1
                print(f"{y}:2st->",buf[i-1],0,buf[i+1])
        buf[1:-1]=out[1:-1]
        print("buf[x]:",x,buf)

    print("x,y:",x,y)

    return out[1:-1]



st= [1,1,1,0,1,1,1,1] #[1,0,0,0,0,1,0,0] # 
days=2

print(inp(st,days)) 

print("*"*50)
import random

print(random.randint)

def mod(a,b):
    #a>b always
    kalan=b
    while (kalan!=0):
        kalan = a%b
        if kalan != 0:
            a=b
            b=kalan
        else:
            return b

def GDC(num,arr):
    arr = sorted(arr)[::-1]
    print("arr:",arr)
    liste=[]
    for i in range(num-1):
        gdc=mod(arr[i],arr[-1]) 
        liste.append(gdc)

    return liste, min(liste)

arr= ra[9,12,16]
num=len(arr)

print(GDC(num,arr)) 