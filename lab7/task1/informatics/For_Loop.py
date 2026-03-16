#A
num1 = int(input())
num2 = int(input())

for i in range(num1, num2+1):
    if i%2==0:
        print(i, end=" ")

#B
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b+1):
    if i%d==c:
        print(i, end=" ")

#C
a1 = int(input())
b1 = int(input())
for i in range(a1, b1+1):
    if int((i**0.5)**2)==i:
        print(i, end=" ")

#D
num3 = input()
d = int(input())
count = 0
for i in num3:
    if (int(i))==d:
        count += 1
print(count)

#E
x = input()
res = 0
for digit in x:
    res+=int(digit)
print(res)

#F
x1 = input()
reversed = int(x1[::-1])
print(reversed)

#G
x2 = int(input())
for i in range(2, x2+1):
    if x2%i==0:
        print(i)
        break

#H
x3 = int(input())
for i in range(1, x3+1):
    if x3%i==0:
        print(i, end=" ")

#I
x4 = int(input())
res1 = 0
for i in range(1, (x4+1)**0.5):
    if x4%i==0:
        res1+=1
print(res1)

#J
sum = 0
for i in range(100):
    x5 = int(input())
    sum += x5
print(sum)

#K
n = int(input())
sum1 = 0
for i in range (n):
    x6 = int(input())
    sum1 += x6
print(sum1)

#L
binary = input()
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[len(binary)-1-i])*(2**i)
print(decimal)

#M
n1 = int(input())
count_zeros = 0
for i in range(n1):
    x7 = int(input())
    if x7==0:
        count_zeros+=1
print(count_zeros)
