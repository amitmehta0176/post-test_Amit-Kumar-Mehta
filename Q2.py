class Person:
    def walk(self):
        print("Person is walking ")
    def talk(self):
        print("person is talking") 
class Teacher(Person):
    def teach(self):
        print("teacher teaches the student")
class Student(Person):
    def study(self):
        print("students study in the classroom")
teacher1=Teacher()
teacher1.teach()
teacher1.walk()
teacher1.talk()   


student1=Student()
student1.study()
student1.walk()
student1.talk()

