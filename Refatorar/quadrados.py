for i in range(1, 100+1):
    s = i**2
    k = s+s
    a = s+s+s
    t = s+s+s+s
    e = s+t
    for n in range(1, 11):
        if n**2 > i+i-1:
            break
    print(s, k, a, t, e)
