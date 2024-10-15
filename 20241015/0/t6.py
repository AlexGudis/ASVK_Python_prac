from t4 import func
from t5 import func_counter
from timeit import Timer

print(Timer(func).autorange())
print(Timer(func_counter).autorange())
