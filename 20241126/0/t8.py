import struct
import random

with open("t8", "wb") as f:
    for i in range(10):
        f.write(struct.pack("f3si", random.random(), bytes((1,2,3)), random.randrange(666000, 181938298)))