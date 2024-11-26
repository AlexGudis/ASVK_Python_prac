import binascii

with open("t8_dump", "rb") as f:
    data = f.read()
    print(binascii.hexlify(data, "\n", 16).decode())


    res = ?
    for addr, i in enumerate(range(0, len(res), 4)):
        print(f"{addr:08x}",":",*res[i:i+4])
