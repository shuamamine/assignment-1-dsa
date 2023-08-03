n = int(input("enter limit!!"))
count = 1
for i in range(0,n): 
    for j in range(0,n-1):
       print(' ', end='')
    for k in range(0,i+1):
        print(chr(65+i), end=' ')
    print(' ')
