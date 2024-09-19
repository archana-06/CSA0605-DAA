def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
        print(f"Pass {i+1}: {arr}")

arr = [29, 10, 14, 37, 13]
print("Initial Array:", arr)
bubble_sort(arr)
print("Sorted Array:", arr)
