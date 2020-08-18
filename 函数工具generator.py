def a_func():
    def b_func():
        print("Hi,I'm b_func!")
    print("Hi,I'm a_func!")
    b_func()
print(a_func())
