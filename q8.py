def fun(i):
    if i%2!=0:
        return i
    else:
        return fun(fun(i-1))
print(fun(200))
