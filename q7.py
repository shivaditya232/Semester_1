fh=open("sample.txt")
y=fh.read()
a="24680"
b="13579"
for i in y:
    if i in a:
        s=open("even.txt","a")
        s.write(i)
    if i in b:
        g=open("odd.txt","a")
        g.write(i)

        