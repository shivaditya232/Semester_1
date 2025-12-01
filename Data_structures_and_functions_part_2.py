#1
"""N=input("enter first set of numbers")
X=input("enter second set of numbers")
k=set(N.split())
l=set(X.split())
n=k.intersection(l)
m=list(n)
m.sort()
print(m)"""

#2
"""correct=input("enter the key")
N=int(input("enter the number of students"))
L=[]
for _ in range(N):
    x=input("enter the options entered")
    length=len(correct)
    count=0
    mark=0
    while count<length-1:
        if correct[count]==x[count]:
            mark+=1
        count+=1
    L.append(mark)
print(L)"""
    
#3
"""hell=[("Helicoradian","Flora",["Valley of Mo'ara","Hallelujah Mountains"]),("Direhorse","Fauna",["Valley of Mo'ara"])]
dict={"Flora":0,"Fauna":0}
L=[]
for i in hell:
    if i[1]=="Flora":
        dict["Flora"]+=1
    elif i[1]=="Fauna":
        dict["Fauna"]+=1
    L=L+i[2]
y=set(L)
z=list(y)
count=0
set1=set()
for i in L:
    if L.count(i)>count:
        count=L.count(i)
        set1.add(i)

for i in set1:
    x=i
L=[]
for i in hell:
    if x in i[2]:
        L.append(i[0])

print(dict)
print(f"Species in {x}:",L)
print("Region with the greatest biodiversity:",x)
"""
#4

"""fing=[("Kuntala Army","Kumar Varma",{"Infantry":5000,"Cavalry":2000,"Archers":3000}),("Mahishmati Army","Bhallaladeva",{"Infantry":8000,"Cavalry":3000,"Archers":4000})]
L=[]
J=[]
M=[]
for i in fing:
    x=i[0]
    j=i[2]
    count=0
    for k in j:
        count+=j.get(k)
    string1=str(x)+":"+str(count)
    L=L+[string1]
    z=j["Cavalry"]
    e=j["Infantry"]
    M.append(e)
    J.append(z)
p=max(J)
u=max(M)

for o in fing:
    y=o[2]
    if y["Cavalry"]==p:
        print("Army with the Largest Cavalry:",o[0])
    if y["Infantry"]==u:
        print("Commander with Most Infantry:",o[1])
print(L)
"""

#5
N=int(input("Enter the number of inputs you want to give"))
L=[]
for i in range(N):
    x=input("enter the input")
    L.append((x))
X=input("enter the country you want")
set1=set()
dict={}
for i in L:
    y=i[1]
    count=0
    string1=""
    string2=""
    for j in L:
        if j[1]==y:
            count+=1
            string1=string1+j[0]
            dict[y]=count
    string2=y+":"+str(count)+","+string1
    set1.add(string2)
list1=list(set1)
list1.sort()
for i in list1:
    print(i)
string3=""
for i in L:
    if X in i[2]:
        string3=string3+i[0]
print(f"Experiments with {X}:")
count1=0
for i in dict:
    if dict.get(i)>count1:
        h=i
print("Most collaborative field:",h)

"""L=[("Microgravity Impact on Cells","Biology","USA:Russia", 2018),("Star Mapping","Astronomy","Canada:Japan:USA",2019),("Fluid Behavior","Physics","Germany",2020),("Galactic Composition","Astronomy","Italy:France:Germany",2021)]"""
    






        
