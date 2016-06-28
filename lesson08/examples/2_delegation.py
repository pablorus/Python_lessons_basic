class Wrapper:
    def __init__(self, object):
        self.wrapped = object  # Сохранить объект

    def __getattr__(self, attrname):
        print('Trace:', attrname)  # Отметить факт извлечения
        return getattr(self.wrapped, attrname)  # Делегировать извлечение


x = Wrapper([1, 2, 3])  # Обернуть список
x.append(4)  # Делегировать операцию методу списка
print(x.wrapped)  # Вывести обернутый объект
x = Wrapper({'a': 1, 'b': 2})  # Обернуть словарь
print(x.keys())  # Делегировать операцию методу словаря