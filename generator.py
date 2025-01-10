def squares(val):
    a=0
    while a<=val:
        yield a**2
        a+=1

for a in squares(10):
    print(a)