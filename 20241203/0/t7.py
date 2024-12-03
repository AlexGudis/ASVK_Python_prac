class C:
    a,b,c = input().split()
    
while check := input():
    match check.split():
        case [C.a, *tail] if 'yes' in tail:
            print("1")
        case [C.b]:
            print("2")
        case [C.c, *tail, C.b]:
            print('3')