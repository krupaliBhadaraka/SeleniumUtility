def fibo_num_at_n(n=5):
    """
    0 1 1 2 3 5 8 13
    :return:
    """
    a, b, = 0, 1
    if n < 0:
        print("Invalid input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # print(fibo_num_at_n(n-1))
        return fibo_num_at_n(n-1) + fibo_num_at_n(n-2)

# Find specific index num from fibonacci number
a = fibo_num_at_n(3)
print(a)

FibArray = [0, 1]

def fib_from_array(n):
    if n < 0:
        print("Incprrect num")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        FibArray.append(fib_from_array(n-2) + fib_from_array(n-1))
        return fib_from_array(n-2) + fib_from_array(n-1)

# print(fib_from_array(10))
# print(FibArray)


def fib_with_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, b + a


# f = fib_with_generator()
#
# for i in f:
#     if i > 10:
#         break
#     else:
#         print(i)
