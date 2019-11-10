import datetime

class Golem:
    def __init__(self,name = None):
    self.name = name 
    self.built_year = datetime.date.today().year

    def say_hi(self):
        print('Hi!')

class runningGolem(Golem):
    def run(self):
        print("can't you see? I'm running...")
    
    def say_hi(self):
        print('Hey! Nice day,Huh?')

rg = runningGolem('Clay')

    




