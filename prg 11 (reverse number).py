def reverse(n, r):
    if n==0:
        return r
    else:
        return reverse(n//10, r*10 + n%10) 
number = int(input("Enter number: "))
reversed_number = reverse(number,0)
print("Reverse of %d is %d" %(number, reversed_number))
