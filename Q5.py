
filename=input("\n entyer filename")    
try:
    with  open(filename,'r') as f:
        lines=f.readlines()
    if len(lines)==0:
        print("file is empty")
    else:
        print(" Total number of  lines",len(lines)) 
except FileNotFoundError:
    print("File doesn't exist")
finally:
    print("operation complete")
