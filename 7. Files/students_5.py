students = []
with open("CS50 ITPWP/7. Files/csv files/students.csv") as file:
    for line in file: 
        name, home = line.rstrip().split(",")
        student = {"name":name, "home": home}
        students.append(student)

# creates a dictionary for each student/house within a list(students).

for student in sorted(students, key=lambda student: student["name"]):
    # this code is equivalent to the get_name function (lambda(anonymous functions))
    print(f"{student['name']} is from {student['home']}")
