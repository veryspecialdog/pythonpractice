import datetime

class Golem:
    __population = 0
    __life_span = 10

    def __init__(self,name = None):
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.__population +=1  #执行一次之后，把这一句改成population += 1 试试看
    
    def say_hi(self):
        print('Hi!')

    def cease(self):
        self.__active = False
        Golem.__population -=1
    
    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem._life_span:
            self.cease()
        return self.__active

g = Golem('Clay')
print(g.population)

