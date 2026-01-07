
L=[]
def load_products():
    
    fh=open("grocery1.txt","r")
    x=fh.readlines()
    for i in x:
        dict1={}
        y=i.split(",")
        dict1["id"]=y[0]
        dict1["name"]=y[1]
        dict1["category"]=y[2]
        dict1["price"]=int(y[3])
        dict1["quantity"]=int(y[4])
        L.append(dict1)
    print(L)
print(load_products())


def display():
    print("ID    NAME   Category   Price    Quantity")
    print("-----------------------------------------")
    for i in L:
        print(f"{i["id"]}   {i["name"]}  {i["category"]} {i["price"]}      {i["quantity"]}")
display()






