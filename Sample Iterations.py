def iteration1(num):
    j = 0
    for k in range (num):
        while j < 2*k:
            j += k
            if k**k == j:
                continue
            else:
                print(j,k)
iteration1(6)

def iteration2(n):
    z = n
    for x in range(3,n,3):
        z = z*10+x
    for y in range(n,n+2):
        z = z*10+y
    return z
print(iteration2(7))