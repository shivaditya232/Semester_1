def test(n):
    if n<10:
        return 1
    return 1 + test(n//10)
print(test(3267))