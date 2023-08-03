n = int(input("enter limit!!"))
count = 1
for i in range(0,n): 
    for j in range(0,i+1): 
         if count%2!=0: 
           print("*", end="") 
         else: 
           print("#", end="")
         count += 1
    print()
