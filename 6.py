def get_k(array):
    n = len(array)
    array_full_sum = sum([i for i in range(n+1)])
    k = array_full_sum - sum(array)
    return int(k)


array = [0, 2, 1, 3, 6, 7, 4, 8, 10, 9, 11]
k = get_k(array)
print(k)
