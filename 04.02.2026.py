#Задача 1
# def f(a, n):
#     if n == 0:
#         return 1
#     return a * f(a, n - 1)
#
# #Задача 2
# def f(n):
#     if n == 0:
#         return 0
#     return n % 10 + f(n // 10)
#
# #Задача 3
# def f(lst):
#     if len(lst) == 1:
#         return lst[0]
#     m = f(lst[1:])
#     return lst[0] if lst[0] > m else m