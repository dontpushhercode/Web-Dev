#double_char
def double_char(str):
  res = ""
  for i in str:
    res+=i*2
  return res

#count_hi
def count_hi(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i:i+2] == "hi":
            count += 1
    return count

#cat_dog
def cat_dog(str):
  return str.count("cat") == str.count("dog")

#count_code
def count_code(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i:i+2] == "co" and s[i+3] == "e":
            count += 1
    return count
  

#end_other
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

#xyz_there
def xyz_there(s):
    for i in range(len(s) - 2):
        if s[i:i+3] == "xyz":
            if i == 0 or s[i-1] != '.':
                return True
    return False