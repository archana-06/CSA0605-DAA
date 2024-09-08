def constant_time_example(n):
    print(f"O(1) Example: The value of n is {n}")

def linear_time_example(n):
    print("O(n) Example: ", end="")
    for i in range(n):
        print(i, end=" ")
    print()

def quadratic_time_example(n):
    print("O(n^2) Example:")
    for i in range(n):
        for j in range(n):
            print(i * n + j, end=" ")
        print()

def logarithmic_time_example(n):
    print("O(log n) Example: ", end="")
    i = 1
    while i < n:
        print(i, end=" ")
        i *= 2  
    print()

def main():
    n = 2
    print("Analyzing Time Complexity:\n")
    constant_time_example(n)
    linear_time_example(n)
    quadratic_time_example(n)
    logarithmic_time_example(n)

if __name__ == "__main__":
    main()
