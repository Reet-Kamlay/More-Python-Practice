def simple_interest(p,r,t):
    return (p*r*t)/100
num1=int(input("Enter principal value: "))
num2=int(input("Enter rate of interest: "))
num3=int(input("Enter time in years: "))
print("The simple interest is: ",simple_interest(num1,num2,num3))
