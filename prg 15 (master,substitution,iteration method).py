def master_theorem_example():
    # Recurrence: T(n) = 2T(n/2) + n
    # This fits the Master Theorem where a = 2, b = 2, and f(n) = n
    # Comparing n^log_b(a) with f(n):
    # Here, n^log_2(2) = n and f(n) = n, so case 2 of the Master Theorem applies.
    # Time complexity is O(n log n)
    print("Using Master Theorem:")
    print("Recurrence relation: T(n) = 2T(n/2) + n")
    print("Time complexity is O(n log n)\n")
def main():
    # Master Theorem example
    master_theorem_example()
if __name__ == "__main__":
    main()

def substitution_method_example():
    # Recurrence: T(n) = 3T(n/2) + n^2
    # Guess a solution: T(n) = O(n^log_b(a)) = O(n^log_2(3))
    # We substitute and verify this guess:
    # Substitution leads to a final complexity of O(n^log_2(3)).

    print("Using Substitution Method:")
    print("Recurrence relation: T(n) = 3T(n/2) + n^2")
    print("Guess: T(n) = O(n^log_2(3))")
    print("Time complexity is O(n^log_2(3))\n")
def main():
    # Substitution Method example
    substitution_method_example()
if __name__ == "__main__":
    main()

def iteration_method_example():
    # Recurrence: T(n) = T(n-1) + 1
    # We expand the recurrence:
    # T(n) = T(n-1) + 1 = T(n-2) + 2 = ... = T(1) + (n-1)
    # This gives us T(n) = O(n)
    print("Using Iteration Method:")
    print("Recurrence relation: T(n) = T(n-1) + 1")
    print("Time complexity is O(n)\n")
def main():
    # Iteration Method example
    iteration_method_example()
if __name__ == "__main__":
    main()

