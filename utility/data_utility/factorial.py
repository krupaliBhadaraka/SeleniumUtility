def num_fact_value(n):
    """
    0 = 0
    1 = 0
    2 = 2
    3 = 6
    4 = 24
    5 = 120
    :return:
    """
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

# num_fact_value(5)

import math

a = math.factorial(5)
print(a)
