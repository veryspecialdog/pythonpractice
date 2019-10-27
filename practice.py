def routine_1():
    print('Routine 1 done.')

def routine_2():
    sub_routine_1()
    sub_Routine_2()
    print('Routine 2 done.')


def sub_routine_1():
    print('Sub-routine 1 done.')

def sub_Routine_2():
    print('Sub-routine 2 done.')

def main():
    routine_1()
    routine_2()
    print('this is the end of program')

if _name_=='_main_':
    main()