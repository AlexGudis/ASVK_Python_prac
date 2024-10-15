
from timeit import Timer
import string 

def f():
    check_gl = set("aeiouy")
    check_sogl = set(string.ascii_lowercase) - check_gl
    s = set("wekhcbwecbw")

    return len(s & check_gl), len(s & check_sogl)
    
    '''
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
    '''


print(Timer(f).autorange())


