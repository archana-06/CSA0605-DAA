def subsets_with_element(S, x):
    S.sort()  # Ensure lexicographical order
    result = []

    def backtrack(start, current_subset):
        if x in current_subset:
            result.append(current_subset[:])
        for i in range(start, len(S)):
            current_subset.append(S[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return result

# Example usage
E = [2, 3, 4, 5]
x = 3
print(subsets_with_element(E, x))
