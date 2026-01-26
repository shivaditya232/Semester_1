fh1=open("sample.txt","r")
fh2=open("sample2.txt","w")
read1=fh1.read()
for i in read1:
    fh2.write(i)
