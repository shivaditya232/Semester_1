def list_operation(lst):
    if not lst:
        return 0
    return lst[0]+list_operation(lst[1:])
print(list_operation([10,20,50,40,30]))


