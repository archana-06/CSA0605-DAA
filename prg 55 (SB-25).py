def subsets(S):
    S.sort()  
    result = []

    def backtrack(start, current_subset):
        result.append(current_subset[:])
        for i in range(start, len(S)):
            if i > start and S[i] == S[i - 1]:
                continue  # Skip duplicates
            current_subset.append(S[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return result

# Example usage
A = [1, 2, 3]
print(subsets(A))
