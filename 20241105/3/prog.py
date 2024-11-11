from copy import deepcopy

MIDDLE = "·"
FULL = "█"


class Maze:
    def __init__(self, n):
        self.matrix = [[FULL] * (2*n + 1) for _ in range(2 * n + 1)]
        for i in range(2 * n + 1):
            for j in range(2 * n + 1):
                if i % 2 and j % 2:
                    self.matrix[i][j] = MIDDLE

    def __setitem__(self, data, value):
        #print(data, "    ===    ", value)
        start, stop = sorted([(data[0], data[1].start),  (data[1].stop, data[2])])
        #print(start, stop)

        # x coords
        if start[0] == stop[0]:
            for j in range(start[1] * 2 + 1, stop[1] * 2 + 2):
                self.matrix[j][start[0] * 2 + 1] = value
        # y coords
        elif start[1] == stop[1]:
            for i in range(start[0] * 2 + 1, stop[0] * 2 + 2):
                self.matrix[start[1] * 2 + 1][i] = value

    def __getitem__(self, data):
        #(row, column)
        start, stop = sorted([(data[1].start * 2 + 1, data[0] * 2 + 1),  (data[2] * 2 + 1, data[1].stop * 2 + 1)])
        #print("In get:", start, stop)
        return self.find(start, stop)
    

    def find(self, p1, p2):
        #print("===NEW FIND===")
        matrix = deepcopy(self.matrix)
        plan = []
        plan.append(p1)
        matrix[p1[0]][p1[1]] = '*'
        #print(plan)
        while plan:
            cur = plan.pop(0)
            matrix[cur[0]][cur[1]] = '*'

            if (cur[0], cur[1]) == (p2[0], p2[1]):
                #print("CONGRATS!!!")
                return True

            #print("up = ", (cur[0]-1, cur[1]))
            if matrix[cur[0]-1][cur[1]] != '*' and matrix[cur[0]-1][cur[1]] == MIDDLE and (cur[0]-1, cur[1]) not in plan:
                plan.append((cur[0]-1, cur[1]))


            #print("right = ", (cur[0], cur[1]+1))
            if matrix[cur[0]][cur[1]+1] != '*' and matrix[cur[0]][cur[1]+1] == MIDDLE and (cur[0], cur[1]+1) not in plan:
                plan.append((cur[0], cur[1]+1))


            #print("down = ", (cur[0]+1, cur[1]))
            #print(matrix[cur[0]+1][cur[1]])
            if matrix[cur[0]+1][cur[1]] != '*' and matrix[cur[0]+1][cur[1]] == MIDDLE and (cur[0]+1, cur[1]) not in plan:
                plan.append((cur[0]+1, cur[1]))


            #print("left = ", (cur[0], cur[1]-1))
            if matrix[cur[0]][cur[1]-1] != '*' and matrix[cur[0]][cur[1]-1] == MIDDLE and (cur[0], cur[1]-1) not in plan:
                plan.append((cur[0], cur[1]-1))
            #print(plan)
        #print("NO WAY")
        return False


    def __str__(self):
        ans = []
        for el in self.matrix:
            ans.append(''.join(el))
            

        return '\n'.join(ans)

'''
m = Maze(4)
print(m)
print(m[0,0 : 1,0],m[0,0 : 2,2],m[1,0 : 1,2])
m[0,0 : 0,3] = m[0,3 : 3,3] = m[3,3 : 3,0] = m[3,0 : 2,0] = m[2,0 : 2,2] = m[1,0 : 1,2] = "·"
print(m)
print(m[0,0 : 1,0],m[0,0 : 2,2],m[1,0 : 1,2])
'''


import sys
exec(sys.stdin.read())