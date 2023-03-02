names = []
with open("CS50 ITPWP/7. Files/txt files/names.txt") as file:
    for line in file: 
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")