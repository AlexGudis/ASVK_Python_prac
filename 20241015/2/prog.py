from math import *

functions = dict()
cnt = 0
ans = []
while True:
    s = input()
    cnt += 1
    if s.split()[0] == 'quit':
        s = s.split('quit ')
        func_actions = s[-1]
        functions['quit'] = [func_actions + '.format(x, y)']
        params = {'x':len(functions), 'y':cnt}
        ans.append(eval(functions['quit'][-1],None,params))
        break
    if s[0] == ':':
        s = s[1:]
        s = s.split()
        func_name = s[0]
        func_params = s[1:len(s) - 1]
        func_actions = s[-1]
        functions[func_name] = func_params + [func_actions]
    else:
        s = s.split()
        params = dict()
        for i in range(len(functions[s[0]]) - 1):
            if s[i+1].replace('.','',1).isdigit() or (s[i+1][0] == '-' and s[i+1].count('-') == 1 and s[i+1].replace('.','',1).replace('-','',1).isdigit()):
                params[functions[s[0]][i]] = float(s[i + 1])
            else:
                params[functions[s[0]][i]] = s[i + 1]
        #print(functions[s[0]][-1], params)
        ans.append(eval(functions[s[0]][-1], None, params))

#print(functions)
for el in ans:
    print(el)