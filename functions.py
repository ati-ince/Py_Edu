def print_name(name):
    print(str(name))


print_name("ali")

#important featue yıu can use *arg input of funtion get all data from outside:
def sum_(*arg_):
    total=0
    for i in arg_:
        total+=i
    return total

out = sum_(0,1,2,3,4,5,6,7,8,9)
print(f"out: {out}")

# be aware to be carry value to function if vallue list or somethig
# you see below carry value of list standart variable not change via sub function but for list somethings diffeerent....
# immutable objects (stabndart variable, string, tuple etc.) can not change but mutable (list etc) can be change

def test_(x,y):
    x[0]=6
    x[1]=7
    y=12

a= [5,3]
b = 4
print (b, a) 
test_(a,b) 
print (b,a)

# generators

# decerators
# mostly use for function parameter getting object like another function.... interesting feature... function call function.

