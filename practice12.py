name=input("What is your name: ")
print("What service do you want sir?")
print("Enter 1 for Police; Enter 2 for Paramedics; Enter 3 for Fire")
num=int(input("Enter the number: "))
if num==1:
    print("Police will reach your destination")
elif num==2:
    print("Paramedics will reach your destination")
elif num==3:
    print("Fire will reach your destination")
else:
    print("Invalid Number")
