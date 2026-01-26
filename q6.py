fh=open("sample.txt","r")
read=fh.read()
count=0
s="abcdefghijklmnopqrstuvwxyz"
for i in read:
    if i not in s and i!="\n":
        count+=int(i)
print(count)
fh=open("sample.txt","a")
fh.write(str(count))


