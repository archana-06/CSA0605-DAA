import itertools
def meet_in_the_middle(arr, target):
    n = len(arr)
    left_half = arr[:n // 2]
    right_half = arr[n // 2:]
    def get_subset_sums(nums):
        subset_sums = []
        for i in range(len(nums) + 1):
            for subset in itertools.combinations(nums, i):
                subset_sums.append(sum(subset))
        return subset_sums
    left_sums = get_subset_sums(left_half)
    right_sums = get_subset_sums(right_half)
    
    right_sums.sort()

    closest_sum = float('inf')
    for left_sum in left_sums:
        low, high = 0, len(right_sums) - 1
        while low <= high:
            mid = (low + high) // 2
            current_sum = left_sum + right_sums[mid]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            
            if current_sum < target:
                low = mid + 1
            else:
                high = mid - 1

    return closest_sum

# Example usage
set1 = [45, 34, 4, 12, 5, 2]
target1 = 42
print(meet_in_the_middle(set1, target1))  

set2 = [1, 3, 2, 7, 4, 6]
target2 = 10
print(meet_in_the_middle(set2, target2))  
