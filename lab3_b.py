import random
import string
def pwd(len):
    res=" "
    str=string.ascii_letters+string.digits+string.punctuation
    for i in range(len):
       res=res+random.choice(str)
    return res
n=int(input("enter the length of a string"))
print(pwd(n))
   

