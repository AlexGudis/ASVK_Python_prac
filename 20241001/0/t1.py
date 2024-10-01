def average(a, *args):
    print((a + sum([el for el in args])) / (1 + len(args)))

average(1,2,3)