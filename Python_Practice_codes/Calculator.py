def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

def calculate(a):
    o=input("")
    if o=="CE":
        return 
    b=float(input(""))
    if o=="+":
        a=add(a,b)
    elif o=="-":
        a=sub(a,b)
    elif o=="*":
        a=mult(a,b)
    elif o=="/":
        a=div(a,b) 
    print("= ",a)   
    calculate(a) 
    
print("Enter no. followed by operator (eg: 5 + 2)\nType CE to exit.")
a=float(input(""))
calculate(a)
      