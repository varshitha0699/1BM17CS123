l=[]
n=int(input("enter number"))
for i in range(1,n+1):
     if n%i==0:
        l.append(i)
print(l)
