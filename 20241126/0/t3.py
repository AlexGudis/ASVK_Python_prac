with open("t3", "r") as f:
    data = f.readlines()


for i in range(int(len(data) / 3) + 1):
    print(data[i],end='')