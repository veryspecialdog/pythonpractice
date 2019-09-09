x=1
while x<=9:
    y=1
    while y<=x:
        print("{}*{}={}\t".format(x,y,x*y),end='')
        y +=1
    print()
    x +=1
print()



names = ['anne','beth','george','damon']
ages = [12,45,32,102]

for i in range(len(names)):
    print(names[i],'is',ages[i],'years old')

print(list(zip(names,ages)))  

from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break




        
        
        
    
    


   
        
        
        
    
    
    
    
