digits=[8,9,9,9]
l=len(digits)
i=l-1
while i-1>=0 and digits[i]==9:
    digits[i]=0
    if digits[i-1]!=9:
        digits[i-1]=digits[i-1]+1
    i=i-1
print(digits)
