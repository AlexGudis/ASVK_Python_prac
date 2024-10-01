def fun(n):
    if n <= 0:
        return 1
    return fun(n - 1)

fun(5)