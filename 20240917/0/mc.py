a = int(input())
match a:
    case a if a % 2 == 0: print("Четное")
    case a: print(a,"--это много", sep='')

    