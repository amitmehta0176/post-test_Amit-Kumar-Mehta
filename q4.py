class InvalidAgeError(Exception):
    pass
 
class InvalidMarksError(Exception):
    pass
 
try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
 
    if age < 15 or age > 30:
        raise InvalidAgeError("Age must be between 15 and 30.")
 
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
 
    print("Student registered successfully!")
 
except InvalidAgeError as e:
    print("Invalid Age Error:", e)
 
except InvalidMarksError as e:
    print("Invalid Marks Error:", e)
 
finally:
    print("Registration process complete.")