class Student: 
    def __init__(self, name, house):
        self.name = name
        self.house = house
        

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name (self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    # Getter - a function for a class that gets some attributes
    @property
    def house(self):
        return self._house

    # Setter - a function in some class that sets some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    

if __name__ == "__main__":
    main()

# decorators, functions that modify the behaviour of other functions