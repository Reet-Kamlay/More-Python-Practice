def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
s="madam"
print("The original string is:")
print(s)
print("The reversed string:")
print(reverse(s))
