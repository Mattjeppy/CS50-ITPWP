with open("CS50 ITPWP/7. Files/txt files/names.txt") as file:
    for line in sorted(file): 
        print("hello,", line.rstrip())