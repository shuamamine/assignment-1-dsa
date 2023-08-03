n=int(input("enter limit : "))
if n==1:
   print(1)
elif n==2:
   print(2)
elif n==3:
    print(6)
else: 
   a=6
   b=3
   in=2
   n-=3
   for i in range(n):
      ans+= b*b
      b+=in
      in+=1
   print(ans)
