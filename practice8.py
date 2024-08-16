a=10
b=10.5
if a%b==0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")

rem=0
counter=1
n=56
while counter<=n:
    d=n%10
    rem=rem*10+d
    n=n/10
    counter+=1
print(int(rem))

value=int(input("Enter a number:"))
if value%7==0:
    print("It is a Buzz number")
else:
    print("It is not a Buzz number")
