#sleep_in
def sleep_in(weekday, vacation):
  return (not weekday) or vacation

#monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

#sum_double
def sum_double(a, b):
  if a==b:
    return (a+b)*2
  return a+b

#diff21
def diff21(n):
  if n<=21:
    return 21-n
  else:
    return 2*(n-21)

#parrot_trouble
def parrot_trouble(talking, hour):
  return talking and (hour<7 or hour>20) 

#makes10
def makes10(a, b):
  return (a==10 or b==10) or a+b==10

#near_hundred
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

#pos_neg
def pos_neg(a, b, negative):
  if negative:
    return a<0 and b<0
  else:
    return (a>0 and b<0) or (a<0 and b>0)

#not_string
def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not "+str

#missing_char
def missing_char(str, n):
  res = ""
  for i in range(len(str)):
    if i==n:
      continue
    else:
      res+=str[i]
  return res

#front_back
def front_back(str):
  if (len(str))<=1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]

#front3
def front3(str):
  if (len(str))<3:
    return str*3
  else:
    return str[:3]*3

