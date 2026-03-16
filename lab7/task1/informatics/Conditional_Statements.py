#A
a = int(input())
b = int(input())

print(a if a>b else b)

#B
year = int(input())

if(year%4==0 and year%100!=0 or year%400==0):
    print("YES")
else:
    print("NO")

#C
true_answer = int(input())
sch_answer = int(input())

if(true_answer==1 and sch_answer!=1):
    print("NO")
else:
    print("YES")

#D
num = int(input())

if(num==0):
    print(0)
elif(num>0):
    print(1)
else:
    print(-1)

#E
num1 = int(input())
num2 = int(input())

if(num1>num2):
    print(1)
elif(num2>num1):
    print(2)
else:
    print(0)