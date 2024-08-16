x=[1,2,3]
counter=0
while counter<len(x):
    print(x[counter]*'%')
    for y in x:
        print(y*'*')
    counter+=1
