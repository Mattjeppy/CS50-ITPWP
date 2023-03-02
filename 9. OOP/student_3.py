# creating a class (data type)
class Student: 
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    # student = Student(), creating an object / instance of class
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    # store attributes within class using . notation
    return student


if __name__ == "__main__":
    main()