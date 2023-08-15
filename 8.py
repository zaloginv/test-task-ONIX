def mult_fact(n):
    sum_of_factorials = 1
    curr_factorial = 1
    for i in range(2, n + 1):
        curr_factorial *= i
        sum_of_factorials *= curr_factorial
    return sum_of_factorials

n = 3
print(mult_fact(n))