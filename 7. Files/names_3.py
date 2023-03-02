with open("CS50 ITPWP/7. Files/txt files/names.txt", "r") as file:
    lines = file.readlines()

for line in lines: 
    print("hello,", line.rstrip())