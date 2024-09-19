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
    right_sums_set = set(right_sums)

    for left_sum in left_sums:
        if (target - left_sum) in right_sums_set:
            return True

    return False

E1 = [1, 3, 9, 2, 7, 12]
target1 = 15
print(meet_in_the_middle(E1, target1))

E2 = [3, 34, 4, 12, 5, 2]
target2 = 15
print(meet_in_the_middle(E2, target2))
