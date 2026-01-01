books=[{"title":"The Hobbit","author":"n","year":1937},{"title":"Harry Potter","author":"aoni","year":2006},{"title":"The Happines","author":"bhriya","year":2000}]
for i in range(len(books)):
    min=books[i]["author"]
    for j in range(i+1,len(books)):
        if books[j]["author"]<min:
            min=books[j]["author"]
            books[i],books[j]=books[j],books[i]
print(books)