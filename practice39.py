x=20
y=10
#1- Addition, 2- Subtraction, 3- Multiplication, 4- Division, 
code=int(input("Enter the code: "))
if code==1:
    print("Addition",x+y)
elif code==2:
    print("Subtraction",x-y)
elif code==3:
    print("Multiplication",x*y)
elif code==4:
    print("Division",x//y)
else:
    print("Wrong input")
