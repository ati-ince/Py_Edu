#use basic definition
class Person:
    name_="ali"
    age_ =12

    def name(self):
        print("name: ", self.name_ )
    
    def age(self):
        print("age: ",self.age_)


#create object
person = Person()

#print variable diretly from class
print(person.age_)

#call class function
person.name()
person.age()





