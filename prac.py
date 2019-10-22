def say_hi(greeting,*names,capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting},{name}!')

say_hi('hello','mike','john','zeo',capitalized= True)
