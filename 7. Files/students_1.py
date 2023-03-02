with open("CS50 ITPWP/7. Files/csv files/students.csv") as file: 
    for line in file: 
        row = line.rstrip().split(",")
# row is a list, rstrip removes whitespace and split seperates the file at the CSV (comma seperated values)
        print(f"{row[0]} is in {row[1]}")