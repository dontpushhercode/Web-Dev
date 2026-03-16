#A
a = list(map(int, input().split()))
print(*a[::2])

#B
arr = list(map(int, input().split()))

for i in arr:
    if i%2==0:
        print(i, end=" ")

#C
arr1 = list(map(int, input().split()))
c = 0

for i in arr1:
    if i>0:
        c+=1
print(c)

#D
arr2 = list(map(int, input().split()))

for i in range(len(arr2)-1):
    if arr2[i+1]>arr2[i]:
        print(arr2[i+1], end=" ")

#E
arr3 = list(map(int, input().split()))

for i in range(len(arr3)-1):
    if arr3[i+1]*arr3[i]>0:
        print(arr3[i], arr3[i+1], sep=" ")
        break

#F
arr4 = list(map(int, input().split()))
c1 = 0

for i in range(1, len(arr4)-1):
    if arr4[i]>arr4[i-1] and arr4[i]>arr4[i+1]:
        c1 += 1
print(c1)

#G
arr5 = list(map(int, input().split()))
biggest = arr5[0]
index = 0

for i in range(1, len(arr5)):
    if arr5[i]>biggest:
        biggest = arr5[i]
        index = i
print(biggest, index)