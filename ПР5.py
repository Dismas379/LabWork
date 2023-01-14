str = "Яблоко Орех Армия Жаба"

for w in str.split():
    if w.endswith("я"):
        print(w)
