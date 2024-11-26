import locale
'''print(locale.getlocale())
print("ывслысытсцутлс".encode("KOI8-R"))'''


s = "вопрос".encode("CP1251")
print(s.decode("KOI8-R"))

s2 = "внимание".encode("CP1251")
print(s2.decode("KOI8-R"))

s2 = "питание".encode("CP1251")
print(s2.decode("KOI8-R"))