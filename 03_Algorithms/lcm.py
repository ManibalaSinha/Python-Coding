# Iterative GCD function
def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# LCM function using GCD
def lcm(a, b):
    return (a * b) // gcd_iterative(a, b)

# Define numbers
a = 36
b = 60

# Calculate GCD and LCM
print(f"GCD of {a} and {b} =", gcd_iterative(a, b))
print(f"LCM of {a} and {b} =", lcm(a, b))
