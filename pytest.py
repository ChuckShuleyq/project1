from time import time
from functools import cache, lru_cache
from sys import setrecursionlimit
setrecursionlimit(10**6)
start_time = time()
@lru_cache
def factorial(n):
    if n <= 0:
        return SyntaxError("Number should be greater than 0")
    if n == 1:
        return n
    return n*factorial(n-1)

print(factorial(1200))
print(time() - start_time)