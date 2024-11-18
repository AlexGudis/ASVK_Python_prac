class Undead(Exception):
    pass


class Skeleton(Undead):
    pass


class Zombie(Undead):
    pass


class Ghoul(Undead):
    pass


ex = [Skeleton(), Zombie(), Ghoul()]

def necro(a):
    raise ex[a % 3]

x,y = eval(input())


for i in range(x,y):
    try:
        necro(i)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")
