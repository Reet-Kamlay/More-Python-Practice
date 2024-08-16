a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b:
    if a>c:
        print("First number is Greater")
    else:
        print("Third number is greater")
elif b>a:
    if b>c:
        print("Second number is greater")
    else:
        print("Third number is greater")
else:
    print("No single is greater")
