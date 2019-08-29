def check(l1,num):
   if num in l1:
      return "true"
   else:
      return "false"
list=[]
n=int(input("enter n value:"))
print("enter {} elements".format(n))
for i in range(n):
     ele=int(input())
     list.append(ele)
k=int(input("enter number:"))
print(check(list,k))

