def find_min_max(arr):
    if not arr:
        return None, None

    min_val = arr[0]
    max_val = arr[-1]
    return min_val, max_val
arr = [2, 4, 6, 8, 10, 12, 14, 18]
min_val, max_val = find_min_max(arr)

print(f"Min = {min_val}, Max = {max_val}")
