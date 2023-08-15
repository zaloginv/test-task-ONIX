def min_max(A, B):
    B, A = ((A + B) / 2 + abs(A - B) / 2), ((A + B) / 2 - abs(A - B) / 2)
    return int(A), int(B)

print(*min_max(5, 2))