def calcsome(x,y):
    return x*y,x/y,x%y,x+y,x-y
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
mul,div,re,add,sub=calcsome(num1,num2)
print("multiplication: ",mul)
print("division: ",div)
print("remainder: ",re)
print("addition: ",add)
print("substraction: ",sub)
