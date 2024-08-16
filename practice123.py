def encrypt(sttr,enkey):
    return enkey.join(sttr)
def decrypt(sttr,enkey):
    return sttr.split(enkey)
mainString=input("Enter the main string: ")
encryptedStr=input("Enter the encryption key: ")
enstr=encrypt(mainString,encryptedStr)
delst=decrypt(enstr,encryptedStr)
destr="".join(delst)
print("The encrypted string is: ",enstr)
print("The string after decryption is: ",destr)
