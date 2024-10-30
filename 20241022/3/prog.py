import itertools
print(*sorted(list(filter(lambda x: x.count('TOR') == 2, list(''.join(el) for el in itertools.product( 'TOR', repeat=int(input()) ))))), sep=', ')
