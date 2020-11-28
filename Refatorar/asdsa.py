
N = 413
for q in range(3, N, 2):
    r1, r2 = divmod((N - pow(q, 2)), (2 * q))
    if pow(q, 2) > N:
        break
    if r2 == 0:
        print(pow(r1, 2), "+", N, "=", N + pow(r1, 2), "o numero", N, "nao é primo")
        break
    if r1 == 1:
        break

