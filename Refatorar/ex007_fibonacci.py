n = 22

t1 = 0
t2 = 1
t4 = 0
print(t1, t2, end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(t3, end=' ')

