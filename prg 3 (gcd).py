def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
num1 = 15
num2 = 5
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}.")
