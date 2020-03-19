# *** we can use more than one methods for use for statements...

# with the help of list etc...
words = ["apple", "orange", "banana", "mellon"] 
for w in words:
    print(w)

# other methd is use range() function... that is like normal loop method like C...
for i in range(0,10,2):
    print(i)

# next method is ugly.. use pyhon like C. But sometimes necessary to use like this.. 
listX = [1,2,3,4,5,11,"224",434,11,",",0]
for j in range(len(listX)): #or listX.__len__()
    print(j)

