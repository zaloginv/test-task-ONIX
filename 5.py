from math import sqrt


def if_replace(A):
    try:
        sqrt(A)
        return -1
    except Exception:
        return 10


B = if_replace(0)
print(B)