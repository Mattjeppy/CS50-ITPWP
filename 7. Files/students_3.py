students = []

with open("CS50 ITPWP/7. Files/csv files/students.csv") as file:
    for line in file: 
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)