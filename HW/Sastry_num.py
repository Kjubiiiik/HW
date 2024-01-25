#In this challenge, you have to establish if a given integer n is a Sastry number. 
#If the number resulting from the concatenation of an integer n with its successor is a perfect square, then n is a Sastry Number.
#Given a positive integer n, implement a function that returns True if n is a Sastry number, or False if it's not.
#Examples
#is_sastry(183) ➞ True
# Concatenation of n and its successor = 183184
# 183184 is a perfect square (428 ^ 2)

n = int(input("Zadejte číslo: "))

def s(n):
    list_of_digits = [int(i) for i in str(n)]
    n2 = n + 1
    list_of_digits2 = [int(i) for i in str(n2)]
    main_list = list_of_digits + list_of_digits2
    number = 0
    for digit in main_list:
        number = number*10 + digit
    main_number = number
    if main_number % 2 == 0:
        return "True"
    elif main_number % 2 != 0:
        return "False"
print(s(n))