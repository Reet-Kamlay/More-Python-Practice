strin=str(input("Enter your sentence: "))
res=0
curr_len=0
n=len(strin)
def longest(strin):
    return max(res,curr_len)
for i in range(0,n):
    if (strin[i]!=''):
        curr_len+=1
        print(max(res,curr_len))
    else:
        res=max(res,curr_len)
        curr_len=0
     
   
    
