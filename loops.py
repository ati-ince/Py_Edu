words = ["ali" , "veli" , "apple"]

#use the list or array for writing all element of it
for i in words:
    #print(i)
    pass

# interesting loop method, write all as you see one by one. ... 
ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"
i=0
for i,ata in enumerate((ata1,ata2,ata3,ata4,ata5)):
    print(i,ata)
