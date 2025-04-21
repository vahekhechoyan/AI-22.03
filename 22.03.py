# 1
# Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.

# def print_down_from_n(n):
#     if n < 1:
#         return
#     print(n)
#     print_down_from_n(n - 1)
# print_down_from_n(5)    


# 2
# Write a function print_characters(s) that prints each character of a string on a new line using recursion.

# def print_characters(s):
#     if s == "":
#         return
#     print(s[0])
#     print_characters(s[1:])

# print_characters("hello")


# 3
# Write a recursive function to calculate the factorial of a number n.
# Factorial is the product of all positive integers from 1 to n. 

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n *factorial(n-1)
    
# print(factorial(5))    


# 4
# Create a recursive function to find the sum of the first n natural numbers.
# The sum of natural numbers from 1 to n is calculated by adding all the numbers in the range

# def sum_natural(n):
#     if n==0:
#         return 0
#     return n+sum_natural(n-1)
# print(sum_natural(5))



# 5
# Write a recursive function to calculate the nth Fibonacci number.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.


# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)

# print (fibonacci(8))


# 6
# Write a recursive function to reverse a given string.
# Reversing a string means rearranging its characters from the last to the first


# def reverse_string(s):
#     if len(s)==0:
#         return ""
#     return s[-1] + reverse_string(s[:-1])

# print(reverse_string("world"))


# 7
# Write a recursive function to check if a string is a palindrome.
# A palindrome is a string that reads the same backward as forward


# def is_palindrom(s):
#     if len(s)<=1:
#         return True 
#     if s[0]!= s[-1]:
#         return False
#     return is_palindrom(s[1:-1])

# print(is_palindrom("madam"))
# print(is_palindrom("hello"))



# 8
# Write a recursive function to calculate the power of a number x raised to n

# def power(x,n):
#     if n==0:
#         return 1
#     return x*power(x,n-1)

# print(power(2,4))




# 9
# Write a recursive function to calculate the sum of all digits in a number

# def sum_of_digits(n):
#     if n==0:
#         return 0
#     return n % 10 + sum_of_digits(n//10)

# print(sum_of_digits(777))



# 10
# Write a recursive binary search algorithm to find the index of a target value in a sorted array.
# Binary search divides the array into halves to find the target more efficiently.


# def binary_search(arr, low, high, target):
#     if low > high:
#         return -1  
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return binary_search(arr, low, mid - 1, target)
#     else:
#         return binary_search(arr, mid + 1, high, target)

# arr = [2, 4, 6, 8]
# target = 6
# result = binary_search(arr, 0, len(arr) - 1, target)
# print(result)



# 11
# Write a recursive function to flatten a list containing nested lists.


# def flaten_list(lst):
#     if len(lst)==0:
#         return []
#     if isinstance(lst[0],list):
#         return flaten_list(lst[0]) + flaten_list(lst[1:])
#     else:
#         return [lst[0]] + flaten_list(lst[1:])
    
# nested = [1, [2, [3, [4]]], 5, 6, 9, 8 ,7]
# print(flaten_list(nested))



# 12
# Write a recursive function to find the maximum element in a list.


# def find_max(lst):
#     if len(lst) ==1:
#         return lst[0]
#     return max(lst[0] ,find_max(lst[1:]))

# print(find_max([1,3,5,6,7,8,5,3]))

