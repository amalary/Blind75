def containsDuplicate(nums):
    hashSet = set()
    
    for num in nums: 
        if num in hashSet: 
            return True 
        hashSet.add(num)   
    return False
            

nums = [11234]

print(containsDuplicate(nums))
