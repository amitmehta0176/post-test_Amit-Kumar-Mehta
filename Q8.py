import os
with open("employees.txt", "w") as f:
    f.write("Amit Singh - 45000\n")
    f.write("Riya Sharma - 52000\n")
    f.write("Raj Patel - 38000\n")
    f.write("Priya Verma - 61000\n")
    f.write("Karan Mehta - 47000\n")
 

print("---- Employee List ----")
with open("employees.txt", "r") as f:
    print(f.read())
 

with open("employees.txt", "a") as f:
    f.write("Sneha Joshi - 55000\n")
    f.write("Vikas Gupta - 43000\n")
 

print("---- Updated Employee List ----")
with open("employees.txt", "r") as f:
    print(f.read())
 

if os.path.exists("employees.txt"):
    print("File exists:", True)
 

os.remove("employees.txt")
print("File deleted.")
print("File exists after deletion:", os.path.exists("employees.txt"))