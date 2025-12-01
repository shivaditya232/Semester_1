string1=input("enter a string")
dict1={'a':1,'e':2,'i':3,'o':4,'u':5}
string2=""
length=len(string1)
for i in range(length):
    if string1[i] in dict1:
        string2=string2+str(dict1.get(string1[i]))
    else:
        string2=string2+string1[i].upper()
print(string2)



       
