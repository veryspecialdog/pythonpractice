import datetime

class Golem:

    def __init__(self,name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')

class Running_Golem(Golem):    #刚刚就说了，这里的圆括号另有用途

    def run(self):
        print("can't you see? I'm running...")
    
    def say_hi(self):          #不再使用Parent Class中的定义，而是使用新的定义
        print('Hey!Nice day,Huh?')

rg = Running_Golem('Clay')

print(dir(rg))

print(hasattr(rg,'built_year'))

    
