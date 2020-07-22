#%load mycode.py
#当前这个code cell中的代码，保存在当前文件夹的mycode.py文件中
#以下代码使用Jupyter命令

def is_prime(n):
    """
    Return a loolean value based upon
    whether the argument n is a prime number.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2,int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

def say_hi(*names,greeting ='Hello',capitalized=False):
    """
    Print a string,with a greeting to everyone,
    :param *names:tuple of names to be greeted.
    :param greeting:'Hello' as default.
    :param capitalized:Whether name should be converted to capitallized before print,False as default.
    :returns:None
    """
    for name in names:
        if capitalized:
            name =name.capitalized()
        print(f'{greeting},{name}!')

