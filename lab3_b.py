import random
import string


def ch(len):
    res=" "
    str1 = string.ascii_letters + string.digits + string.punctuation
    res=res+random.choice(string.ascii_uppercase)
    res=res+random.choice(string.digits)
    res=res+random.choice(string.ascii_lowercase)
    for i in range(len-3):
        res = res+random.choice(str1)
    str_var = list(res)
    random.shuffle(str_var)
    print(''.join(str_var))

n = int(input("enter the number"))
ch(n)
