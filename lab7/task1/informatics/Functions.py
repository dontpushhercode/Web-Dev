#A
def min4(a, b,  c, d):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    if d < min:
        min = d
    return min

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))

#B
def power(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res

a = int(input())
n = int(input())
print(power(a, n))

#C
def xor(a, b):
    if a == b:
        return 0
    else:
        return 1

a = int(input())
b = int(input())
print(xor(a, b))