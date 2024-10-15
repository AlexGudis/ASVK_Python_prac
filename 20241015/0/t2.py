check = set("aeiouy")
s = set(input())
gl_cnt = 0
sogl_cnt = 0
for el in s:
    if el.islower():
        if el in check:
            gl_cnt += 1
        else:
            sogl_cnt += 1
print(gl_cnt)
print(sogl_cnt)
