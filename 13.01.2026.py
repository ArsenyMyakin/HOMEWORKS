from functools import *
@lru_cache(None)
def f(n):
    if n>30: return f(n-6)+2048
    if n<=30: return 3*(g(n-5)+13)
@lru_cache(None)
def g(n):
    if n>=221337: return 2*n+50
    if n<221337: return g(n+11)-48
for i in range(10000000000000000):
    f(i)
for i in range(10000000000000000):
    g(i)
print(f(5078))