def func(text1,text2):
    f1=open(text1,'r')
    f2=open(text2,'r')
    str1=f1.read()
    str2=f2.read()
    l1=[]
    l2=[]
    l1=str1.split(',')
    l2=str2.split(',')
    for i in l1:
        for j in l2:
            if i==j:
                print('OVERLAPPING')
                return
func('t1','t2')
            

