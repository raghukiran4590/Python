import sys

# print(sys.getrecursionlimit())

def fact(n):
    if n == 0:
        return 1
    ans = n * fact(n-1)
    return ans

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)

# print(fact(5))
# print(fib(6))

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

print(countdown(6))