### LIST ###
list1 = ['ali', 'cal', 1,3, 's', [23,"1"]]
print (list1)

list1.append('veli') #only add single element...
print(list1)

list1.extend(['kim' , 1]) #add with matrix
print(list1)

#lets write in a loop
for l in list1:
    print(l)

# with range() fn you can create a list too.... normally range output belong range class.....
list2=list(range(100))
print(list2)

list3 = list(range(0,100,3)) #also create like series... with different start stop point and increse amount
print(list3)

list4 = list(range(99,-10,-7)) #more, you can reach negative applications... :)
print(list4)
