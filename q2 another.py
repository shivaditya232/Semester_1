fh=open("sample.txt","r")
for i in fh :
    if i!="\n":
        print(i,end="")
    