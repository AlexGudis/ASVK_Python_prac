a = list(range(5, 16))
b = [chr(i) for i in range(ord('a'), ord('k') + 1)]
# a[4:8] = [chr(i) for i in range(ord('a'), ord('k') + 1)][-5:]
a[4 : 8] = b[-5:]
