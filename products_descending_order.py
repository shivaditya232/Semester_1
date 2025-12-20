products=[{"id":101,"name":"laptop","price":900,"stock":12},{"id":205,"name":"keyboard","price":25,"stock":85},{"id":150,"name":"monitor","price":180,"stock":30}]
for i in range(len(products)):
    min=products[i]["price"]
    for j in range(i,len(products)):
        if products[j]["price"]<min:
            min=products[j]["price"]
            products[i],products[j]=products[j],products[i]
            

print(products)