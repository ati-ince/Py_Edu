'''
You have to write a function Staircase which takes an integer N (1<=N<=50), the height of the
staircase, as its argument and prints a staircase as shown in the example.
N = 5
OUTPUT:
    #
   ##
  ###
 ####
#####

Note that there is no leading space in the last line of the output.

'''
def StairCase(number):
    #condition 1<= and 50>= so, 
    for i in range(number):
        output= " "*(number-i-1)+"#"*(i+1)
        print(output)


StairCase(10)

# 5 min spend