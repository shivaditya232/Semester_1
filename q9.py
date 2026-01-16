def flow(num):
    if num>0:
        print('before',num)
        flow(num-2)
        print('after',num)
    else:
        print('base case')
flow(6)
