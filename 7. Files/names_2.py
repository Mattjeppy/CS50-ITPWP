name = input("What's your name? ")

with open("CS50 ITPWP/7. Files/txt files/names.txt", "a") as file:
    file.write(f"{name}\n")