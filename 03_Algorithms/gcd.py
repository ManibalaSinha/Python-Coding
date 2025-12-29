def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Define values for a and b
a = 36
b = 60

# Now call the function
print(f"GCD of {a} and {b} =", gcd_iterative(a, b))

