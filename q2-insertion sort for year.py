books=[{"title":"The Hobbit","author":"tolkien","year":2037},{"title":"Harry Potter","author":"J.K Rowlling","year":2006}]
for i in range(1,len(books)):
    key=books[i]["year"]
    j=i-1
    while j>=0 and books[j]["year"]>key:
        books[j+1]=books[j]
        j-=1
    books[j+1]["year"]=key
print(books)
