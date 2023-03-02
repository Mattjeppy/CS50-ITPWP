students = []
with open("CS50 ITPWP/7. Files/csv files/students.csv") as file:
    for line in file: 
        name, house = line.rstrip().split(",")
        student = {"name":name, "house": house}
        students.append(student)

# creates a dictionary for each student/house within a list(students).

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")