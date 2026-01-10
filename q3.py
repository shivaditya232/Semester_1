def demo(n):
    if n==0:
        return 0
    return n + demo(n-1)
print(demo(5))