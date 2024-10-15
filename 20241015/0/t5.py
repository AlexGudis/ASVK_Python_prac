from collections import Counter

def func_counter(s="abcd abcd abcd"):
    return Counter(s.split())

