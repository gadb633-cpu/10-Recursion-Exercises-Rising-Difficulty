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

# 3. Build a List From 1 to N
def numbers_to_n(n):
    if n ==0:
        return []
    
    return numbers_to_n(n-1) +[n]
print(numbers_to_n(5))

# 4. Count Items in a List
def count_items(lst):
    if lst==[]:
        return 0
    lst.pop(0)
    num_len =1
    return num_len + count_items(lst)
print(count_items(["a", "b", "c"])) 

# 5. Count Even Numbers in a List
def count_evens(numbers):
    if numbers==[]:
        return 0
    num = numbers.pop(0)
    if num%2==0:
        return 1+ count_evens(numbers)
    else:
        return 0+count_evens(numbers)
print(count_evens([4, 7, 10, 3, 8]))

