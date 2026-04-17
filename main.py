class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

    def is_passed(self):
        if self.grade >= 60:
            return True
        return False


def main():
    s1 = Student("Ali", 17, 75)
    s2 = Student("Vali", 16, 45)

    students = [s1, s2]

    for s in students:
        s.display_info()
        if s.is_passed():
            print("Status: Passed")
        else:
            print("Status: Failed")
        print("----------------")


main()
