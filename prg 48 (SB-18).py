def merge_sort(arr):
    global comparison_count
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    global comparison_count
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        comparison_count += 1
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

comparison_count = 0
arr = [12, 4, 78, 23, 45, 67, 89, 1]
sorted_arr = merge_sort(arr)

print(','.join(map(str, sorted_arr)))
print(f"Number of comparisons: {comparison_count}")
