def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_numbers = [0, 1]
        for i in range(2, length):
            fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2]
                               )
        print(fib_numbers)
