import csv 

students = []
with open("CS50 ITPWP/7. Files/csv files/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    # this code is equivalent to the get_name function (lambda(anonymous functions))
    print(f"{student['name']} is from {student['home']}")
