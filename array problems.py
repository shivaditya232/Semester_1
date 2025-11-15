
"""for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]==array[j]:
            array.remove(array[j])
print(array)"""
"""j=1
for i in range(len(array)):
    j=i+1
    while j<=len(array)-1:
        if array[i]==array[j]:
            array.remove(array[j])
        j+=1
    
print(array)"""

"""set1=set(array)
array2=arr.array('i',set1)
print(array2)"""
"""array2=arr.array('i')
for i in range(len(array)-1,-1,-1):
    array2=array2+arr.array('i',[array[i]])
print(array2)"""
"""average=sum(array)/len(array)
print(average)
count=0
for i in range(len(array)):
    if array[i]>average:
        count=count+1
print(count)"""
"""total=0
max=0
for i in range(len(array)):
    total=total+array[i]
    if array[i]>max:
        max=array[i]
print(total)
print(max)
length=len(array)
consecutive=length-1
count=0
while count<consecutive:
    percentage_increase=((array[count+1]-array[count])/(array[count]))*100
    count+=1
    print(f"percentage increase of {count} days",percentage_increase)"""
"""array2=arr.array('d')
for i in range(len(array)):

    if 0<=array[i]<=100:
        array2=array2+arr.array('d',[array[i]])
        
print(array2)
array2.clear()
for i in range(len(array)):
    if 0<=array[i]<=100:
        array2=array2+arr.array('d',[array[i]])
    else:
        array2=array2+arr.array('d',[(array[i-1]+array[i+1])/2])
print(array2)
"""
"""import array as arr
N=int(input("enter the number of elements you want to enter"))
L1=[]
L2=[]

for i in range(N):
    x=int(input("enter your ordered item"))
    L1=L1+[x]
for j in range(N):
    y=int(input("enter the items currently in stock"))
    L2=L2+[y]
array1=arr.array('i',L1)
array2=arr.array('i',L2)
print(array1)
print(array2)
for i in range(len(L1)):
    if L1[i] in L2:
        print(f"The item {L1[i]} can be fulfilled")"""

"""set1={1,2,3,4,5,6}
set2={3,4,5,6,7,8}
y=set1.difference(set2)
print(y)
print(set1)
set1.difference_update(set2)
print(set1)
dict=tuple(zip(set1,set2))
print(dict)"""
"""L1=input("enter the list")
l2=list(set(L1))
print(l2)
dict={}
for i in range(len(l2)):
    dict[l2[i]]=L1.count(L1[i])
print(dict)"""

"""set1=input("enter a set")
set2=input("enter a set")
set4=set(set2)
set3=set(set1)"""
"""x=set3.intersection(set4)
y=set3.difference(x)
z=set4.difference(x)
print(y)
print(z)"""

"""if set1 in set2 and set1!=set2:
    print("set2 is a superset of set1")
else:
    print("it is not a superset")
"""
"""count=0
for a in set3:
    if a in set4:
        count+=1
if count>0:
    print("False")
else:
    print("True")"""
"""count=0
for a in set3:
    count+=1
print(count)"""
"""x=set3.union(set4)
y=len(x)-len(set4)
print(x)
print(y)"""
"""b_count=0
o_count=0
t_count=0
for i in set3:
    if i in set4:
        b_count+=1
for i in set3:
    if i not in set4:
          o_count+=1
for j in set4:
    if j not in set3:
        o_count+=1
print(o_count)"""
"""tuple1=("star",)
print(type(tuple1))
print(set4.symmetric_difference(set3))"""
"""thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x,thisset)"""
dict1={"navikesh":100,"sudharshan":100,"shivaditya":0}
print(dict1.values())
print(dict1.items())


    
    






