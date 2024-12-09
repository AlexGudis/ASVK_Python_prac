import sys
import math

s = sys.stdin.read()
s = s.split('\n')

arifmetic_commands = ['add', 'sub', 'div', 'mul'] # add ....
if_commands = ['ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'] # ifge ....
basic_commands = ['stop', 'store']
all_commands = ['add', 'sub', 'div', 'mul'] + ['stop', 'store'] + ['ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'] + ['stop', 'store']

labels = {} # label : command_number
commands = [] 
usable_lab = []
variables = {} # name : value

command_number = 0
for i in range(len(s)):
    s[i] = s[i].strip()
    line = s[i].split()

    if line and line[0].endswith(':'): # строка начинается на метку
        labels[line[0][:-1]] = len(commands) # запомним номер команды для перехода на метку
        line = line[1:]

    commands.append(line) # добавляю любую команду --> дальше некоманды будут в игноре

    if line and line[0] in if_commands and len(line) == 4:
        #print(f'adding = {line[3]}')
        usable_lab.append(line[3])

#print(commands)
#print(labels)
#print(usable_lab)

# Если найден переход на несуществующую метку --> завершаем работу
for el in usable_lab:
    if el not in labels:
        exit(0)


index = 0
while index < len(commands):
    #print(f'Current varaibles = {variables}')
    match commands[index]:
        case ['store', data, var]:
            #print('STORE', data, var)
            try:
                val = float(data)
                variables[var] = val
            except Exception:
                variables[var] = 0

        case [op, source, operand, priem] if op in arifmetic_commands:
            #print('OP', op, source, operand, priem)
            try:
                variables.setdefault(source, 0)
                variables.setdefault(operand, 0)
                variables.setdefault(priem, 0)
                if op == 'add':
                    variables[priem] = variables[source] + variables[operand]
                if op == 'sub':
                    variables[priem] = variables[source] - variables[operand]
                if op == 'div':
                    variables[priem] = variables[source] / variables[operand]
                if op == 'mul':
                    variables[priem] = variables[source] * variables[operand]
            except Exception:
                #print('EXCEPTION!!!')

                variables[priem] = math.inf

        case [cmp, source, oper, metka] if cmp in if_commands:
            #print('CMP', cmp, source, oper, metka)
            variables.setdefault(source, 0)
            variables.setdefault(oper, 0)

            if cmp == 'ifeq':
                # проверяем операцию на корректность и сразу переходим на нужную команду
                if variables[source] == variables[oper]:
                    index = labels[metka]
                    continue

            
            if cmp == 'ifne':
                # проверяем операцию на корректность и сразу переходим на нужную команду
                if variables[source] != variables[oper]:
                    index = labels[metka]
                    continue


            if cmp == 'ifgt':
                # проверяем операцию на корректность и сразу переходим на нужную команду
                if variables[source] > variables[oper]:
                    index = labels[metka]
                    continue


            if cmp == 'ifge':
                # проверяем операцию на корректность и сразу переходим на нужную команду
                if variables[source] >= variables[oper]:
                    index = labels[metka]
                    continue


            if cmp == 'iflt':
                # проверяем операцию на корректность и сразу переходим на нужную команду
                if variables[source] < variables[oper]:
                    index = labels[metka]
                    continue


            if cmp == 'ifle':
                # проверяем операцию на корректность и сразу переходим на нужную команду
                if variables[source] <= variables[oper]:
                    index = labels[metka]
                    continue

        case ['out', what]:
            print(variables[what])
        
        case ['stop']:
            exit(0)

        
    index += 1



    

    


