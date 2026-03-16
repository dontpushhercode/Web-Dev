#count_evens
def count_evens(nums):
    res = 0
    for i in nums:
        if i%2==0:
            res+=1
    return res

#big_diff
def big_diff(nums):
    return max(nums)-min(nums)

#centered_average
def centered_average(nums):
    return (sum(nums) - min(nums) - max(nums)) // (len(nums) - 2)

#sum13
def sum13(nums):
    total = 0
    skip = False
        
    for x in nums:
        if x == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        total += x
    return total

#sum67
def sum67(nums):
    total = 0
    skip = False
    for x in nums:
        if x == 6:
            skip = True
            continue
        if skip:
            if x == 7:
                skip = False
            continue
        total += x
    return total

#has22
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False