transactions=[{"id":1,"amount":2000,"location":"NY"},{"id":2,"amount":1500,"location":"Chennai"}]
for i in range(1,len(transactions)):
    key=transactions[i]["amount"]
    j=i-1
    while j>=0 and transactions[j]["amount"]>key:
        transactions[j+1]=transactions[j]
        j-=1
    transactions[j+1]["amount"]=key
print(transactions)
