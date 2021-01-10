for num in range(1, 20):
    if num == 10:
        print(f'9 x {num:>2} = {9 * num:>3} ({9 * num})')
    else:
        print(f'9 x {num:>2} = {9 * num:>3} ({num - len(str(num))}{((num - len(str(num))) - 9 * len(str(num))) * -1})')

# [print(f'9 x {num:>2} = {9 * num:>3}  ({num - len(str(num))}{((num - len(str(num))) - 9 * len(str(num))) * -1})')
# for num in range(1, 20)]


# a cada casa decimal a sequencia muda

# 9 x 4(uma casa)
# 4 - 1 = 3
# 3 (4, 5, 6, 7, 8, 9) = 6 até 9 apartir do 3
# 36

# 9 x 14(duas casas)
# 14 - 2 = 12
# 12 (13, 14, 15, 16, 17, 18) 6 até 18 apartir do 12
