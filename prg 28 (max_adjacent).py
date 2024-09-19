"""You are given an array nums consisting of integers. You are also given a 2D array queries, where queries[i] = [posi, xi].
For query i, we first set nums[posi] equal to xi, then we calculate the answer to query i which is the maximum sum of a subsequence
of nums where no two adjacent elements are selected. Return the sum of the answers to all queries. Since the final answer may be very
large, return it modulo 109 + 7. A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.
"""
MOD = 10**9 + 7

def max_non_adjacent_sum(nums):
    include, exclude = 0, 0
    for num in nums:
        new_include = exclude + num
        new_exclude = max(include, exclude)
        include, exclude = new_include, new_exclude
    
    return max(include, exclude)

def sum_of_answers(nums, queries):
    total_sum = 0
    
    for query in queries:
        posi, xi = query
        nums[posi] = xi
        total_sum = (total_sum + max_non_adjacent_sum(nums)) % MOD
    
    return total_sum

# Main function to test
def main():
    nums = [1, 2, 3, 4]
    queries = [[1, 5], [0, 6], [3, 2]]
    print(f"Sum of answers: {sum_of_answers(nums, queries)}")  

if __name__ == "__main__":
    main()









