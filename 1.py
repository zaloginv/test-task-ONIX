def f(A):
    res = 1
    for i in range(2, A):
        res *= i
    return res

print(f(10))