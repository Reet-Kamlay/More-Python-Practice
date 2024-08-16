def oct2others(n):
    numString=str(n)
    decNum=int(numString,8)
    print("Number in decimal form:",decNum)
    print("Number in binary form:",bin(decNum))
    print("Number in hexadecimal form:",hex(decNum))
num=int(input("Enter the octal nunber: "))
oct2others(num)
