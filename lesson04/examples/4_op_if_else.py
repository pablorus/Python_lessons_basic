d = {"name": "Вася"}
# d = {}

# Пример из предыдущего объяснения:
# Получить имя, если имени нет, то "безымянный"
if d.get("name"):
    name = d["name"]
else:
    name = "Безымянный"
print(name)

# Или так - с помощью тернарного if else
print(d.get("name") if d.get("name") else "Безымянный")

# Синтаксис
# value_if_logic_true if logic else value_if_logic_false
# Т.е. возвращается или первое значение, или второе, в зависимости от значения выражения после if
