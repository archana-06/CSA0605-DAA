def merge(nums, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    left_part = nums[left:mid+1]
    right_part = nums[mid+1:right+1]
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if left_part[i] <= right_part[j]:
            nums[k] = left_part[i]
            i += 1
        else:
            nums[k] = right_part[j]
            j += 1
        k += 1
    while i < n1:
        nums[k] = left_part[i]
        i += 1
        k += 1
    while j < n2:
        nums[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)

def sort_array(nums):
    merge_sort(nums, 0, len(nums) - 1)
    return nums
nums = [5, 2, 3, 1]
print(sort_array(nums))  # Output: [1, 2, 3, 5]

