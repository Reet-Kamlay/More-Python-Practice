a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
if a>b and a>c:
    print("First Number is Greater")
elif b>a and b>c:
    print("Second Number is Greater")
elif c>a and c>b:
    print("Third Number is Greater")
else:
    print("No single is greater")
