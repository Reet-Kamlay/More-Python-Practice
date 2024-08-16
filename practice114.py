def retSeries(init,step):
    return init,init+step,init+2*step,init+3*step
ini=int(input("Enter the initial value: "))
st=int(input("Enter the step value: "))
t1,t2,t3,t4=retSeries(ini,st)
print(t1,t2,t3,t4)
