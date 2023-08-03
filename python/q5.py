a = []
n =  int(input("enter size of array : "))
print("enter elements of array : ")
for i in range(n):
    ele = int(input())
    a.append(ele)
k = int(input(" enter location :"))
p=  int(input("enter new element"))
a.insert(k,p)
print(a)
