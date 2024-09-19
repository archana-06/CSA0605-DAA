def findKthPositive(arr, k):
    missing_count = 0
    prev_num = 0
    for num in arr:
        missing_in_between = num - prev_num - 1
        if missing_count + missing_in_between >= k:
            return prev_num + (k - missing_count)
        missing_count += missing_in_between
        prev_num = num
    return arr[-1] + (k - missing_count)
arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositive(arr, k))  
