def sort_even_odd_positions(nums):
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 == 1]
    result = [0] * len(nums)
    even_index, odd_index = 0, 1  
    for num in evens:
        result[even_index] = num
        even_index += 2
    for num in odds:
        result[odd_index] = num
        odd_index += 2
    return result
nums = [3, 1, 2, 4, 7, 8]
print(sort_even_odd_positions(nums))  
