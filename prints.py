# show some usage of print methods... 

# format method start with py3.x
value = 12
print("the value 1 is {}".format(value)) # this method orgnally use strng methıd "format".... little bit foxy :)

v_str = "13"
#other is more familiar like C ... 
print("the value 2 is %d and also have string expression %s "  % (value,v_str) )

#other important print feature is after py3 the standart add f'xxx{smt}' for show like below:
print(f"the value is:{value}", f" and also some string stattement is:{v_str}") #more useful most of applications. The types is not concern of us... 