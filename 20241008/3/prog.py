cnt = 0
cont_in = []
water_cnt = 0
gas_cnt = 0
while cnt != 2:
    s = input()
    if all(el == '#' for el in s):
        cnt += 1
    water_cnt += s.count('~')
    gas_cnt += s.count('.')

    cont_in.append([el for el in s])

W = len(cont_in)
H = len(cont_in[0])

water_level = W - 2
water_fill = 0
if water_cnt % water_level == 0:
    water_fill = water_cnt / water_level
else:
    water_fill = int(water_cnt / water_level) + 1
cont_ans = [['#'] * W for _ in range(H)]

gas_fill = H - 2 - water_fill
for i in range(1, H - 1):
    dot_inp = False
    if gas_fill > 0:
        dot_inp = True
        gas_fill -= 1
    for j in range(1, W - 1):
        if dot_inp:
            cont_ans[i][j] = '.'
        else:
            cont_ans[i][j] = '~'


full = (W - 2) * (H - 2)
for el in cont_ans:
    print(*el, sep='')

gas_points = int((H - 2 - water_fill) * (W - 2))
water_points = int(water_fill * (W - 2))


if gas_points >= water_points:
    print(f"{'.' * 20} {gas_points}/{(W - 2) * (H - 2)}")
    print(f"{'~' * round(20 * water_points / gas_points)}{' ' * (20 - round(20 * water_points / gas_points))} {' ' * (len(str(gas_points)) - len(str(water_points)))}{water_points}/{(W - 2) * (H - 2)}")

    #line_length = int((H - 2 - water_fill) * (W - 2)) + 1 + len(str(gas_fill * (W - 2)))+ len(str(full))
else:
    #line_length = int(water_fill * (W - 2)) + 1 + len(str(water_fill * (W - 2)))+ len(str(full))
    print(f"{'.' * round(20 * gas_points / water_points)}{' ' * (20 - round(20 * gas_points / water_points))} {' ' * (len(str(water_points)) - len(str(gas_points)))}{gas_points}/{(W - 2) * (H - 2)}")
    print(f"{'~' * 20} {water_points}/{(W - 2) * (H - 2)}")





    