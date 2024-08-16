n1=int(input("Enter the beginning number: "))
n2=int(input("Enter the ending number: "))
sum=0
for i in range(n1,n2+1):
    sum=sum+i
print("Sum of numbers from",n1,"to",n2,"is",sum)
