#A
a = int(input())
b = int(input())
c = (a*a+b*b)**0.5
print(c)

#B
num = int(input())
next_num = num + 1
prev_num = num - 1
print("The next number for the number", num, "is", next_num, sep=" ", end=".\n")
print("The previous number for the number", num, "is", prev_num, sep=" ", end=".\n")

#C
schoolchildren = int(input())
apples = int(input())

result = apples // schoolchildren
print(result)

#D
remainder = apples % schoolchildren
print(remainder)

#E
v = int(input())
t = int(input())
print((v*t)%109)