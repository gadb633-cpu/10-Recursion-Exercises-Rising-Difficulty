# 10 Recursion Exercises — Rising Difficulty
# 1. Power of a Number
def power(base, exponent):
    if exponent ==0:
        return 1
    exponent -=1
    return base* power(base, exponent)
print(power(2,4))

# 2. Factorial
def factorial(n):
    if n ==0:
        return 1
    
    return n*factorial(n-1)
print(factorial(5))
