class Golem:
    def __init__(self,name=None):
        self.name = name
        self.built_year = datatime.data.today().year 
    
    def say_hi(self):
        print('Hi!')
print(g=Golem('Clay'))

