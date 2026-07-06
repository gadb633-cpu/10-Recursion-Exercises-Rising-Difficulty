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

# 6. Find Maximum Number
def max_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if numbers[0]>numbers[1]:
        numbers.pop(1)
    else:
        numbers.pop(0)
    return max_number(numbers)    

print(max_number([4, 9, 2, 11, 6]))    

# 7. Reverse a String
def reverse_string(text):
    if text=="":
        return ""
    word = text[-1:]
    return word+reverse_string(text[0:-1])
print(reverse_string("python"))

#8. Check Palindrome
def is_palindrome(text):
    x = text
    if len(text)<=1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False
print(is_palindrome("level"))    

# 9. Count How Many Times an Item Appears
def count_value(lst, value):
    if len(lst)==0:
        return 0
    count =lst.pop(0)
    if count ==value:
        return 1 + count_value(lst, value)
    else:
        return count_value(lst, value)
print(count_value([1, 2, 2, 3, 2], 2))   

# # 10. Fibonacci
# def fibonacci(n,a,b):
    
#     # lst = list(range(n))
#     # if n> len(lst):
#     #     return
#     # rounds=0
#     if n==0:
#         return 0
#     a = b
#     b = a+b
#     return fibonacci(n-1,a,b)


# print(fibonacci(10,0,1)) 

    


    



