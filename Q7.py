students = {"Amit", "Riya", "Raj", "Priya", "Amit", "Riya", "Sneha", "Karan"}
 
print("\nSet (duplicates removed):", students)
 
students.add("Vikas")
students.add("Neha")
print("After adding 2 students:", students)
 
marks_dict = {
    "Amit": 82,
    "Surya": 85,
    "Alok" : 45,
    "Priya": 91
}
 
print("\nResult:")
for name, marks in marks_dict.items():
    if marks >= 75:
        print(name, "- Distinction")
    elif marks >= 60:
        print(name, "- Pass")
    else:
        print(name, "- Fail")