t = "qwe"

match t.split():
    case []:
        print("Empty")
    case [("qwe" as string) | ("rty" as string)]: # Это называется АЛЬТЕРНАТИВА
        print("No doubt", string)
    case [str(x)]:
        print("List of 1 str")
    case [x]:
        print("A list of 1")
    case [_, *tail]:
        print("List with tail", tail)