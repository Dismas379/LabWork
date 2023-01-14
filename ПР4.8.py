n = int(input("Введите число:"))

for i in range(n):
    if n > 9:
        break
    for j in range(1, i+2):
        print(j, end='')
    print()
