
phrase = "we are going today OR tomorrow ... "

#calculate the length of string...
print(phrase.__len__())
print(len(phrase))

#have lot of tring calss function we have can use in applications
capitilize_ = phrase.capitalize()
upper_ = phrase.upper()
lower_ = phrase.lower()

print(capitilize_)
print(upper_)
print(lower_)

### important methods with characters -> with strings...
#lover, upper -> we use above
#islover, isupper, endswith("."),startswith(),capitalize() -> just for check the characters lover, higher or end with "." and convert first latter to Upper character 
# also can use title() to convert all sub-string first character to Capitilize... "like python is a language".title() -> "Python Is A Language"
#sorted -> sort with alphabetically
 #if we want to sort using turkish or other language use like this: 
import locale
locale.setlocale(locale.LC_ALL, "tr_TR.utf8")
response = sorted(set("çekirdek"), key=locale.strxfrm) #use sample string , firstly delete same charakter ... not necessary.. 
print(response)
#reversed -< rotate the characters 
#replace -> chance character with something..
name="huseyin"
name_ch = name.replace("h","H")
print(name_ch)
#split() -> divide string into sub-string
statement="hello, today I am going to new universe"
for i,st in enumerate(statement.split(" ")):
    print (i,st)
#strip(), lstrip(), rstrip()
# may be pretty important methods they are .... delete unnecessary element in character list ... (I can say string is a character list)
stringRAW="2 gün süreyle ilan edilen sokağa çıkma yasağına büyük oranda uyulurken, kimi vatandaşlar yasağa aldırış etmedi."
print(stringRAW.strip(","))
print(stringRAW.replace(",",""))
#join() -> combine sub string opbject to one string like " ".join(["ali","go","outside"]) -> "ali go outside"
#count() -> count specific letter count in the string like:
statement = "ali go to the school for learn python or just #staryhome4covid"
print(statement.count("o"))

#index() -> pretty important usage we have... 
print(statement.index("o")) # you seee we can find the index of element.... do in loop

o_str=set()
for i,st in enumerate(statement):
    try: 
        o_str.add(statement.index("o",i))
    except:
        pass
print(sorted(o_str)) # show the index of "o" character.....

# find() -> more useful than index because there is no error .. if can not find just getting -1 like below:
o_str=set()
for i,st in enumerate(statement):
    o_str.add(statement.find("o",i))
o_str.remove(int(-1))
print(sorted(o_str)) # show the index of "o" character.....

#encode() -> use for create string with any codec/encode
name= "hüseyin".encode("utf-8") #or all others... 

#translate() -> use for convert character to other like if you use specific character like türkish ş,ç -> want to convert s,c etc... use translate and prepare a dixtionary for convertion.

#####*****

