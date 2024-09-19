"""Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i]
is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].A subarray may only include each element
of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist
i <= k1, k2 <= j with k1 % n == k2 % n.
"""
def max_subarray_sum_circular(nums):
    def kadane_max(arr):
        current_sum = max_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    def kadane_min(arr):
        current_sum = min_sum = arr[0]
        for num in arr[1:]:
            current_sum = min(num, current_sum + num)
            min_sum = min(min_sum, current_sum)
        return min_sum
    total_sum = sum(nums)
    max_kadane = kadane_max(nums)
    min_kadane = kadane_min(nums)
    if total_sum == min_kadane:
        return max_kadane
    return max(max_kadane, total_sum - min_kadane)
def main():
    nums1 = [5, -3, 5]
    print(f"Maximum sum of circular subarray (nums1): {max_subarray_sum_circular(nums1)}")  

    nums2 = [-2, -3, -1]
    print(f"Maximum sum of circular subarray (nums2): {max_subarray_sum_circular(nums2)}")  

    nums3 = [1, -2, 3, -2]
    print(f"Maximum sum of circular subarray (nums3): {max_subarray_sum_circular(nums3)}") 

if __name__ == "__main__":
    main()









