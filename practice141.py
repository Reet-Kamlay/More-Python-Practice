def palindrome(s):
    return s==s[::-1]
s=str(input("Enter your string: "))
ans=palindrome(s)
if ans:
    print("True")
else:
    print("False")
