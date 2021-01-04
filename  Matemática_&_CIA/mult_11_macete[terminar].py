[print(num * 11) for num in range(1, 20)]

for num in range(1, 20):
    result = str(num * 11)

    if len(result) != 2:
        print(f'{result[0]}{int(result[0]) + int(result[len(result) - 1])}{result[-1]}')
    else:
        print(result)
