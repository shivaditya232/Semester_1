x=input("enter the file you want to count")
fh=open(x,"r")
y=fh.read()
count=0
s=y.split()
h="1234567890"
for i in s:
    if i not in h:

        count+=1
print(count)
        