books=[{"title":"The Hobbit","author":"aditya","year":2037},{"title":"Harry Potter","author":"moni","year":2006}]
def autocomplete_function(x):
    for i in books:
        if i["title"].startswith(x):
            print(i["title"])
        break

x=input("enter the starting word")
autocomplete_function(x)