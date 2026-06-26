class student:
    def __init__(self, name, age):
        self.stu_name = name
        self.stu_age = age

    def display_info(self):
        print("Name:", self.stu_name)
        print("Age:", self.stu_age)

stu1 = student("Sumit", 19)
stu1.display_info()