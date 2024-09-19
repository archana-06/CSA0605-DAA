def numIdenticalPairs(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    good_pairs = 0
    for k in count.values():
        if k > 1:
            good_pairs += k * (k - 1) // 2
    
    return good_pairs

print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))  
