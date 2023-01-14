n = int(input("Введите кол-во цифр в цикле:"))
b = 1
c = 0

for i in range(1, n + 1):
    tecush = b * i
    c += tecush
    b = tecush

print(c)
