#A
n = int(input())
i = 1
while i*i <= n:
    print(i*i, end=" ")
    i += 1

#B
n1 = int(input())
i1 = 2
while i1<=n1:
    if n1%i1==0:
        print(i1)
        break

#C
n2 = int(input())
x = 1

while x <= n2:
    print(x, end=" ")
    x *= 2

#D
n3 = int(input())
while n3!=1:
    if n3%2==0:
        n3=n3//2
    else:
        print("NO")
        break

if n3==1:
    print("YES")

#E
n4 = int(input())
n5 = 1
counter = 0
while n5<n4:
    n5*=2
    counter += 1
print(counter)