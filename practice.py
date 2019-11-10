import datetime

class Golem:
    def _init_(self,name=None):
        self.name = name
        self.built_year = datetime.date.today().year
    
    def say_hi(self):
        print('Hi!')

g = Golem('Clay')

print(g.name)



