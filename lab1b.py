def fibo(num):
   n1=0
   n2=1
   count=0
   if num==0:
      print("enter correct input")
   elif num==1:
      print(n1)
   else:
     print(n1)
     print(n2)

     while(count<num):
                 
         c=n1+n2
         print(c) 
         n1=n2
         n2=c
         count+=1
print("enter the number")
n=int(input())
fibo(n)
