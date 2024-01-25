#In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1:
#The beginning of the sequence is this:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
#The function fib_fast(num) returns the fibonacci number Fn, of the given num as an argument.

num = int(input("Zadejte kolikrát chcete provést Fib. posloupnost:"))

def Fast_Fib(num):
    Fib_num1 = 0
    Fib_num2 = 1
    M = 1
    Fn = 0

    while num != M:
        Fn = Fib_num1 + Fib_num2        
        Fib_num1 = Fib_num2
        Fib_num2 = Fn
        M += 1
    if num == M:
        return Fn
print(Fast_Fib(num))