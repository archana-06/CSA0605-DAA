# Non-recursive function to calculate sum of first n natural numbers
def non_recursive_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
def main():
    n = 10
    result = non_recursive_sum(n)
    print(f"Non-recursive sum of first {n} natural numbers: {result}")

if __name__ == "__main__":
    main()
    
# Recursive function to calculate factorial of n
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def main():
    n = 5
    result = recursive_factorial(n)
    print(f"Recursive factorial of {n}: {result}")

if __name__ == "__main__":
    main()
