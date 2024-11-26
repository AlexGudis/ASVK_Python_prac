# Сериализация


import pickle
print(pickle.dumps(12324421))
data = pickle.dumps([12324421,"WER",5.3113],protocol=0)
print(pickle.loads(data))


class C:
    a = 1


c = C()

c.b = 123
data = pickle.dumps(c,protocol=0)
print(pickle.loads(data).b)
