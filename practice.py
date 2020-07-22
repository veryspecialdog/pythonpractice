def say_hi(*names):
    for name in names:
        print(f'Hi,{name}!')

names = ('mike','John','zeo')
say_hi(*names)

a_string ='Python'
say_hi(*a_string)

a_range =range(10)
say_hi(*a_range)

a_list = list(range(10,0,-1))
say_hi(*a_list)

a_dictionary ={'ann':2321,'mike':8712,'joe':7610}
say_hi(*a_dictionary)