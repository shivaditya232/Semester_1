str1=input("enter a string")
list1=list(str1)
length=len(str1)
count_uppercase=0
count_lowercase=0
for i in range(length):
    if list1[i].isupper():
        list1[i]=list1[i].lower()
        count_uppercase+=1
    elif str1[i].islower():
        list1[i]=list1[i].upper()
        count_lowercase+=1
    
percentage=((length-count_uppercase-count_lowercase)/length)*100
for i in list1:
    print(i,end='')
print(percentage)
