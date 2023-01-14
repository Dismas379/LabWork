a = int(input("Введите число:"))
b = int(input("Введите число:"))
for i in range(a-int((a%2)==0), b-1, -2):
    print(i)
