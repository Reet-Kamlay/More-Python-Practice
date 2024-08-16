def show_choice():
    print("\n Menu")
    print("1.add")
    print("2.substract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def main(a,b):
    while (true):
        show_choice()
        choice=int(input("Enter choice: "))
if choice=="1":
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("addition=",add(a,b))
elif choice=="2":
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("substract",substract(a,b))
elif choice=="3":
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("multiply",multiply(a,b))
elif choice=="4":
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print("divide",divide(a,b))
    if y==0:
        print("Error can't divide")
    else:
        print("divide=",divide(x,y))
    elif choice=="5":
    break
else:
    print("you don't have any further choice")
