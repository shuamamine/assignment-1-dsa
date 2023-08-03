a = []
n =  int(input("enter size of array : "))
print("enter elements of array : ")
for i in range(n):
    ele = int(input())
    a.append(ele)
  b = []
for i in range(n):
  if a[i] not in b[i+1:size]:
    b.append(a[i])
print(b)
