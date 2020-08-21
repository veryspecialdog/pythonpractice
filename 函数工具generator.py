def a_decorator(func):
    def wrapper():
        print('we can do sth.before a func is called....')
        func()
        print('....and we can do sth.after it is called...')
    return wrapper()

def a_func():
    print("Hi,I'm a_func!")

print(a_func())
print(a_decorator(a_func))