def merge_reverse(A, B):
    a = len(A)
    b = len(B)
    i = a - 1
    j = b - 1

    while i >= 0 and j >= 0:
        if A[i] >= B[j]:
            print(A[i])
            i -= 1
        else:
            print(B[j])
            j -= 1

    while i >= 0:
        print(A[i])
        i -= 1

    while j >= 0:
        print(B[j])
        j -= 1


A = [1, 3, 6, 7, 9]
B = [2, 4, 11, 12]
merge_reverse(A, B)