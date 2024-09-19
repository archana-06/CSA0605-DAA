def median_of_medians(arr, k):
    def partition(arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
    
    def select(arr, left, right, k):
        if left == right:
            return arr[left]
        
        pivot_index = median_of_medians(arr, left, right)
        pivot_index = partition(arr, left, right, pivot_index)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(arr, left, pivot_index - 1, k)
        else:
            return select(arr, pivot_index + 1, right, k)
    
    def median_of_medians(arr, left, right):
        if right - left < 5:
            return partition5(arr, left, right)
        
        for i in range(left, right + 1, 5):
            sub_right = min(i + 4, right)
            median5 = partition5(arr, i, sub_right)
            arr[median5], arr[left + (i - left) // 5] = arr[left + (i - left) // 5], arr[median5]
        
        mid = (right - left) // 10 + left + 1
        return select(arr, left, left + (right - left) // 5, mid)
    
    def partition5(arr, left, right):
        sub_array = sorted(arr[left:right + 1])
        mid = len(sub_array) // 2
        return left + sub_array[mid]

    return select(arr, 0, len(arr) - 1, k - 1)

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k1 = 6
print(median_of_medians(arr1, k1))  
