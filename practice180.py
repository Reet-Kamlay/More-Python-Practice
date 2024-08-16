def increment(n):
    n.append([49])
    return n[0],n[1],n[2],n[3]
L=[23,35,47]
m1,m2,m3,m4=increment(L)
print(L)
print(m1,m2,m3,m4)
print(L[3]==m4)
