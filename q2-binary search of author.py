x=input("enter the author")
books=[{"title":"The Hobbit","author":"aditya","year":2037},{"title":"Harry Potter","author":"moni","year":2006}]
lower=0
higher=len(books)-1
flag=True
L=[]
while lower<=higher:
    mid=(lower+higher)//2
    if x==books[mid]["author"]:
        L.append(books[mid]["title"])
        break
    elif x<books[mid]["author"]:
        higher=mid-1
    elif x>books[mid]["author"]:
        lower=mid+1
print(L)
        