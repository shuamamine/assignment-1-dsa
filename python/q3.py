n = int(input("enter limit!!"))
c = 1
for i in range(0,n): 
    for j in range(i,n-1):
       print(' ', end='')
    for k in range(0,i+1):
        print(c, end=' ')
        c=c+1
    print(' ')
