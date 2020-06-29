import random
n = 10
a_list =[random.randrange(1,100) for i in range(n)]
print(f'a_list comprehends {len(a_list)} random numbers:\n',a_list)

a_list.sort()
print('the list sorted:\n',a_list)

a_list.sort(reverse=True) #reverse参数，默认值是False
print('the list sorted reversely:\n',a_list)

import random
n = 10
a_list = [chr(random.randrange(65,91)) for i in range(n)]
#chr()函数会返回指定ASCII码的字符，ord('A')是65
print(f'a_list comprehends {len(a_list)} random string elements:\n',a_list)

a_list.sort()
print('the list sorted:\n',a_list)

a_list.sort(reverse=True) #reverse参数，默认值是False
print('the list sorted reversely:\n',a_list)

b_list = [chr(random.randrange(65,91))+chr(random.randrange(97,123)) for i in range(n)]

print(f'b_list comprehends {len(b_list)} random string elements:\n',b_list)

b_list.sort()
print('sorted:\n',b_list)

b_list.sort(key=str.lower,reverse=True)
#key参数，默认值是None
#key=str.lower的意思是：先将字母全都转换成小写，在进行比较排序
#但是，这样做不会改变原值
print('the sorted reversely:\n',b_list)

import random
n=3
a_list = [random.randrange(65,91) for i in range(n)]
b_list = [chr(random.randrange(65,91)) for i in range(n)]
print(a_list)
c_list = a_list + b_list +a_list*2

print(c_list)

c_list.append('100')
print(c_list)
print()
print(a_list)
a_list.clear()
print(a_list)

print()
print(a_list)
a_list.clear()
print(a_list)

#复制一个列表
d_list = c_list.copy()
print(d_list)
del d_list[6:8]
print(d_list)
print(c_list)

e_list = d_list
del e_list[6:8]
print(e_list)
print(d_list)

print(a_list)
a_list.extend(c_list)
print(c_list)

print(a_list)
a_list.insert(1,'example')
a_list.insert(3,'example')
print(a_list)

