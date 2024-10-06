def Pareto(args):
    ans = []
    for i in range(len(args)):
        for j in range(len(args)):
            if i != j and args[i][0] <= args[j][0] and args[i][1] <= args[j][1] and (args[i][0] < args[j][0] or args[i][1] < args[j][1]):
                break
        else:
            ans.append(args[i])
    return tuple(ans)


inp = eval(input())
print(Pareto(inp))
