import math as foobar
print(foobar.sqrt(4))

x,y,z = 1,2,3
print(x,y,z)

x,y=y,x
print(x,y,z)

values =1,2,3
print(values)

x,y,z = values
print(x)

name = input('what i your name?')
if name.endswith('Gumby'):
    if name.startwith('Mr.'):
        print('hello,mr. gumnby')
    elif name.startswith('Mrs.'):
        print('hello,mrs.gumby')
    else:
        print('hello,gumby')
else:
    print('hello,stranger')
