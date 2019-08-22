print("enter the number of elements")
n=int(input())
l1=[]
l2=[]
for i in range(n):
  print("enter element:")
  ele=int(input())
  l1.append(ele)
for x in l1:
   if x%2==0:
     l2.append(x)
print("even elements",l2)

