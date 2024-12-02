import sys


data = sys.stdin.buffer.read()
N = data[0]
tail = data[1:]
sorted_parts = sorted([tail[round(i * len(tail) / N):round((i + 1) * len(tail) / N)] for i in range(N)])
result = bytes([N]) + b''.join(sorted_parts)
sys.stdout.buffer.write(result)