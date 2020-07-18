import os

with open('test-file.txt','w') as f:
    f.write('first line\n second line\n third line\n')

with open('test-file.txt','r') as f:
    for line in f.readlines():
        print(line)
        

