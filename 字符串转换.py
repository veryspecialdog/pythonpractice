v=[1,2,3,4,5,6,7,8,9]
v.reverse()
v1=str(v)[2:7]
v2=v1[::-1]
v3=v2[2:3]
v4=int(v3)
v5="{num:b}".format(num=v4)
v6="{num:d}".format(num=v4)
v7="{num:o}".format(num=v4)
print(v5,v6,v7)














