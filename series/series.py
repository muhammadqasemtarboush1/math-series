#fibbonacci sequence 0,1,1,2,3,5,8,13....
#Lucas Numbers 2,1,3,4,7,11,18...
#sum_series custome series

def fibonacci(num):
    # The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer
    # is determined by summing the preindex_ious two.
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# print((fibonacci(9)))

def lucas(num):
    #  Function that returns the nth index_alue in the lucas numbers Again,
    if num == 0:
        return 2
    if num == 1:
        return 1
    else:
        return lucas(num-1) + lucas(num-2)


def sum_series(num, index_1=0, index_2=1):
    if num == 0:
        return index_1
    if num == 1:
        return index_2
    else:
        return sum_series(num-1, index_1, index_2) + sum_series(num-2, index_1, index_2)

print(sum_series(20,2,4))

