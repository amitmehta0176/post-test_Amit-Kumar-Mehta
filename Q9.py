import json
 
students = [
    {"name": "Amit",  "age": 20, "city": "Delhi",   "course": "BCA",  "marks": 85},
    {"name": "Riya",  "age": 21, "city": "Mumbai",  "course": "BBA",  "marks": 65},
    {"name": "Raj",   "age": 19, "city": "Pune",    "course": "BSc",  "marks": 72},
    {"name": "Priya", "age": 22, "city": "Bhopal",  "course": "MCA",  "marks": 55},
]
 
# Save to JSON 
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
 
print("\n---- Students with Marks > 70 ----")
 
# Read the file 
with open("students.json", "r") as f:
    data = json.load(f)
 
for s in data:
    if s["marks"] > 70:
        print(s["name"], "-", s["marks"])
 
print("\nTotal number of students:", len(data))