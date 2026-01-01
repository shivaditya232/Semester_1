books=[{"title":"The Hobbit","author":"tolkien","year":1937},{"title":"Harry Potter","author":"J.K Rowlling","year":2006}]
for i in range(len(books)):
    for j in range(0,len(books)-1-i):
        if books[j+1]["title"]<books[j]["title"]:
            books[j+1],books[j]=books[j],books[j+1]
print(books)