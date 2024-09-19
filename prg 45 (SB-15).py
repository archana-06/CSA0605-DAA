def find_min_max(arr):
    if not arr:
        return None, None

    min_val = arr[0]
    max_val = arr[0]

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

a = [5, 7, 3, 4, 9, 12, 6, 2]
min_val, max_val = find_min_max(a)

print(f"Min = {min_val}, Max = {max_val}")
