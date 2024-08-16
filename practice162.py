x='apple,pear,peach,grapefruit'
y=x.split(',')
for z in y:
    if z<'m':
        print(str.lower(z))
    else:
        print(str.upper(z))
