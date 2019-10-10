import operator

# Sıralama
dictionary = {'b': 1, 'x': 10, 'a': 8, 'y': 3}

# Anahtar'lara göre
# 1
sorted(dictionary.items(), key=operator.itemgetter(0))
# print [('a', 8), ('b', 1), ('x', 10), ('y', 3)]
# 2 (lambda)
sorted(dictionary.items(), key=lambda kv: kv[0])
# print [('a', 8), ('b', 1), ('x', 10), ('y', 3)]

# Değerlere göre
# 1
sorted(dictionary.items(), key=operator.itemgetter(1))
# print [('b', 1), ('y', 3), ('a', 8), ('x', 10)]
# 2 (use lambda)
sorted(dictionary.items(), key=lambda kv: kv[0])
# print [('b', 1), ('y', 3), ('a', 8), ('x', 10)]


# Unpacking
def unpack(*args, **kwargs):
    print(args)
    print(kwargs)


unpack(**dictionary)
# Çıktı
"""
()
{'b': 1, 'x': 10, 'a': 8, 'y': 3}
"""
unpack(*dictionary)
# Çıktı
"""
('b', 'x', 'a', 'y')
{}
"""
#Girdi
sozluk = {"İsim":"Enes"}
# Çıktı
{"İsim":"Enes"}
#Girdi
yenisim = "Mazlum"
sozluk.setdefault("İsim", []).append(yenisim)
#Çıktı
{"İsim":"Mazlum,Enes"}