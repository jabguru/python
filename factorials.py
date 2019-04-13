def factorial():

    # counter = 1
    result = 1
    n = int(input("Put the number you want for find the factorial: "))

    x = n

    if n is 1:
        result = 1
    else:

        # while counter <= x:
        #     result = result * n
        #     counter += 1
        #     n -= 1

        for g in range(x):
            result = result * n
            n -= 1

    return result


print(factorial())
