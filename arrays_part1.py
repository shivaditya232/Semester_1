#1
""" N=int(input("enter a number"))
dict1={}
for i in range(1,N+1):
    dict1[i]=i**2
print(dict1)"""
#2
"""dict1={}
inp=int(input("enter the number of pairs you want to input"))
for i in range(inp):
    key=input("enter the key")
    value=int(input("enter the value"))
    dict1[key]=value
print(dict1)
count=0
for i in dict1:
    count+=dict1[i]
print(count)"""

#3
"""string1=(input("enter a string"))

string2=string1.split(' ')
tuple1=tuple(string2)
set1=set(string2)
dict1={}
print(string2)
print(tuple1)
print(set1)
for i in set1:
    dict1[i]=tuple1.count(i)
print(dict1)"""
#4
"""dict1={"Atomic Number":1,"Melting Point":14,"Boiling Point":20}
dict2={"Atomic Number":2,"Melting Point":1,"Boiling Point":4}
dict3={"Atomic Number":3,"Melting Point":453,"Boiling Point":1603}
Dict={"H":dict1,"He":dict2,"Li":dict3}
print(Dict)
def State(Element,Temperature):
    if Dict[Element]['Melting Point']<Temperature<Dict[Element]['Boiling Point']:
        print("Liquid")
    elif Dict[Element]['Melting Point']>Temperature:
        print("Solid")
    elif Temperature>Dict[Element]['Boiling Point']:
        print("Gas")
Element=input("Enter element symbol")
Temperature=int(input("enter temperature"))
State(Element,Temperature)"""

#5
"""dict1={}
inp=int(input("enter the number of pairs you want to input"))
for i in range(inp):
    key=input("enter the key")
    value=float(input("enter the value"))
    dict1[key]=value
print(dict1)
firstmax=0
secondmax=0
thirdmax=0
for i in dict1:
    if dict1[i]>firstmax:
        thirdmax=secondmax
        secondmax=firstmax
        firstmax=dict1[i]
        
    elif secondmax<dict1[i]<firstmax:
        thirdmax=secondmax
        secondmax=dict1[i]
        firstmax=firstmax
    elif dict1[i]>thirdmax:
        thirdmax=dict1[i]
        secondmax=secondmax
        firstmax=firstmax
for i in dict1:
    if dict1[i]==firstmax:
        print(i, firstmax)
for i in dict1:
    if dict1[i]==secondmax:
        print(i, secondmax)
for i in dict1:
    if dict1[i]==thirdmax:
        print(i, thirdmax)
"""
converter={"INR":1,"EUR":102,"USD":88,"AED":24}
x=int(input("How much money do you have"))
y=input("which currency you have")
z=input("which currency you want to convert")
for i in converter:
    if y==i:
        j=converter[i]
    if z==i:
        k=converter[i]
s=x/k*j
print(s)

        



