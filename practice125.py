def arCalc(x,y):
    return x+y,x-y,x*y,x/y,x%y
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
add,sub,multi,div,mod=arCalc(num1,num2)
print("The addition of numbers is: ",add)
print("The substraction of numbers is: ",sub)
print("The multiplication of numbers is: ",multi)
print("The division of numbers is: ",div)
print("The modulus of numbers is: ",mod)
