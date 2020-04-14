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

# some good method for creating data -> for example create first 100 sqr number
sqr_list = [i**2 for i in range(1,101)] #same method can be use with set, tuples etc... 
print(sqr_list)

# some list test
a= [[1,2],['a',4],[0,"hello"]]
print(type(a))
print(type(a[0])) #as we see list in list we used.... 

# summition of list
list1= [1,2,3,4,5]
list2=["fdsdfd","gfgfg","34dd"]
list3= [[1,2],['a',4],[0,"hello"]]
print(list1+list2) #intereseting... just add end of the last element of 1st list...
print(list2+list3) #yes... same stuation just adding the last...

#copy the list
list1 = [1,2,3,4,5]
list2= ["jnkj","5656","fdf"]

list3 =list1.copy()
list4 = list(list1)
list5=list1
print(id(list1),id(list3),id(list4),id(list5)) #we can see list1 and list5 is same element did not copy it... 

# all methods #
#.append() -> add a element but be carefull, if you add a list using append you add hole list be a singel element to end of first list ....
#.extend() -> add list element to first list one by one.. like -> list1=[1,2,3], list1.extend(['a',5,7]) -> list1 >> [1,2,3, 'a', 5,7 ]
#.index(n) -> getting n. element of list ... you can say like this -> list[n] == list.index(n+1)
#.insert(n,x) -> insert or change the value... lets try... 
liste= [1,2,3,4,5]
liste.insert(1,12)
print(liste) 
liste.insert(72,22) # you can see if the index not match with number of element List ... just add end of the list .
print(liste)
#.pop(n), .remove(n) or del list[n]-> drop and delete n element of list
#.reverse() -> rotate the list order 180degree -> but list[::-1]   -> using this method more usefulll... 
#.count() -> how many element
#.sort() -> pretty importat ... sorting the list using number order or alphabet order or ASCII table nuömber. Using in different way:
people = [{'name':'chandan','age':20,'salary':2000},
          {'name':'chetan','age':18,'salary':5000},
          {'name':'guru','age':30,'salary':3000}] 
print(people) # -> lets sorting....
import operator
people.sort(key=operator.itemgetter('age')) ; print(people)
people.sort(key=operator.itemgetter('salary')) ; print(people[::-1])

### TUPLE ###
tupple1 = (1,2,3,4,5)
print(tupple1)
tupple2 = tuple([1,2,3,4,5,6]) # same as you see
print(tupple2)
tupple3 = tupple2 + tupple1
print(tupple3)
tupple4 = tupple3 + tuple([12,'a',15]) # we can combine like this too... Important issue is summition of same data type we have to use.... 

#let learn all methods of  data structure objects.... 
print([i for i in dir(list) if not "_" in i])
print([i for i in dir(tuple) if not "_" in i])
print([i for i in dir(set) if not "_" in i])
#####*****

### DICTIONARY ###
a=dict({'name':'ali'})
b=set('a')

print(type(a),type(b))
print(a,b)

print(a['name'])

#dictionary comprehension has common usage like list comprehension:
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sozluk = {i: harfler.index(i) for i in harfler}
print(sozluk)

### methods of dictionary
#.keys(), .values() -> keys:values  -> getting data from dict
#fromkeys() ->  dict.fromkeys(list/tuple, "value") -> it will be used for creaing a new dict using list or tuple ...
#.update() -> use for update the specific dict keys:values -> you can create again like before but that time change the id... use update method.. 
sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")} ; print(sepet, id(sepet))
sepet.update({"meyveler": ("muz", "armut"), "sebzeler": ("domates", "fasulye")}) ; print(sepet, id(sepet))
#####*****

list1 = [1,2,3,4,5,6] ; print(list1,id(list1))
list2 = [9,8,7,6,5,4]

list1 = list2.copy() ;  print(list2,id(list2))
