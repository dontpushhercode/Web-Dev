#string_times
def string_times(str, n):
  return str*n

#front_times
def front_times(str, n):
  if (len(str))<3:
    return str*n
  else:
    return str[:3]*n

#string_bits
def string_bits(str):
  return str[::2]

#string_splosion
def string_splosion(s):
    res = ""
    for i in range(len(s)+1):
        res += s[:i]
    return res


#last2
def last2(s):
    if len(s) < 2:
        return 0
    
    last2_sub = s[-2:]
    count = 0
    
    for i in range(len(s)-2):
        if s[i:i+2] == last2_sub:
            count += 1
            
    return count

#array_count9
def array_count9(nums):
  count = 0
  for i in nums:
    if i==9:
      count+=1
  return count

#array_front9
def array_front9(nums):
  if len(nums)<4:
    for i in nums:
      if i==9:
        return True
  else:
    for i in range(4):
      if(nums[i]==9):
        return True
  return False

#array123
def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

#string_match
def string_match(a, b):
    count = 0
    min_len = min(len(a), len(b))
    for i in range(min_len - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1            
    return count
