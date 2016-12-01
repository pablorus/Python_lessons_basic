import collections

# -= Counter (Счетчик) =- 

# Создание
a = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
b = collections.Counter({'a':2, 'b':3, 'c':1})
c = collections.Counter(a=2, b=3, c=1)
print(a==b==c)

# Пополнение
c = collections.Counter(['a', 'b'])
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a':1, 'd':5})
print('Dict    :', c)


# Доступ
for key in sorted(c):
    print(key, c[key])

# Counter не вызывает исключение KeyError для несуществующих элементов.
# Если значения нет - он возвращает 0.
print(c['e'])

c.update({'f': -1})


# most_common() возвращает n элементов с сортировкой по количеству
c = collections.Counter()
with open('alice.txt', 'rt') as f:
    for line in f:
        words = [s.strip(',.!?:;)\'"').lower() for s in line.split()]
        c.update(words)

for letter, count in c.most_common(5):
    print ('%s: %7d' % (letter, count))


# С Counter можно работать как с множествами
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('C1:', c1)
print('C2:', c2)

print('\nКомбинирует счетчики:')
print(c1 + c2)

print('\nВычитает счетчики:')
print(c1 - c2)

print('\nПересечение (выбирает положительные минимумы):')
print(c1 & c2)

print('\nОбъединение (выбирает максимум):')
print(c1 | c2)




# -= OrderedDict (Отсортированный словарь) =-
# Словарь, запоминающий положение своих элементов
# Если новый элемент перезаписывает существующий - позиция не меняется.
# Удаление элемента и его последующая вставка перемещает его в конец.
print ('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print (k, v)

# При сравнении сортированнаго словаря учитывается положение элементов:
d1 = d.copy()
print('Equal:', d == d1)

d1.move_to_end('c')
print('d1:', d1)

print('Equal:', d == d1)



# -= defaultdict (словарь со значением по умолчанию) =-
# collections.defaultdict([default_factory[, ...]])
# Возвращает новый словареподобный объект, возвращающий по умолчанию результат
# функции default_factory

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

print(list(d.items()))



# -= namedtuple (именованный кортеж) =-
# collections.namedtuple(typename, field_names, verbose=False, rename=False)
# field_names - строка, в которой имена полей идут через пробел и/или через 
# запятую. Таккже можно использовать последовательность строк: ['x', 'y']

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p) # Point(x=11, y=22)

Person = collections.namedtuple('Person', 'name age gender')
p = Person('Bob', 40, 'male')
print(p) # Person(name='Bob', age=40, gender='male')

params = ['Василий', 33, 'муж.']
p = Person._make(params)
print(p) # Person(name='Василий', age=33, gender='муж.')

# Возвращает элементы в виде сортированного словаря
print(p._asdict())

# Возвращает новый кортеж, в котором заменены значения
p = p._replace(name='Василиса', gender='жен.')
print(p)

# _fields
# Возвращает кортеж имен полей
Color = collections.namedtuple('Color', 'red green blue')
Pixel = collections.namedtuple('Pixel', Point._fields + Color._fields)

p = Pixel(10, 20, 100, 100, 100)
print(p) # Pixel(x=10, y=20, red=100, green=100, blue=100)















