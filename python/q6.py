a = []
n =  int(input("enter size of array : "))
print("enter elements of array : ")
for i in range(n):
    ele = int(input())
    a.append(ele)
val = int(input(" enter index of element to be deleted"))
a.pop(val)
print(a)
