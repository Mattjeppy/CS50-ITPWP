with open("CS50 ITPWP/7. Files/csv files/students.csv") as file: 
    for line in file: 
        name, house = line.rstrip().split(",")
        # you can unpack data simultaneously into two variables
        print(f"{name} is in {house}")