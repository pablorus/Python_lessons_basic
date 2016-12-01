import itertools

# -= бесконечные последовательности =-

# itertools.count(start=0, step=1) 
# возвращает бесконечный генератор, начиная от start с шагом step
for i in itertools.count(1, 2):
    print(i)
    if i > 100:
        break

# itertools.cycle(iterable)
# Бесконечно повторяет заданную последовательность:
tango = itertools.cycle([1, 2, 3])
for i in range(100):
    print(next(tango), end=' ')
print()

# itertools.repeat(element, times=0) 
# повторяет элемент, если times задано, то times раз

lst = list(map(pow, range(10), itertools.repeat(2)))
print(lst) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# -= контроль за итераторами =-

# Возвращать пока..
# itertools.takewhile(predicate, iterable)
# Создает итератор, возвращающий элементы из iterable до тех пор, пока
# predicate истинен
g = itertools.takewhile(lambda n: n<10, itertools.count())
lst = [i for i in g] 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Срезы
# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop[, step])
# cоздает итератор, который возвращает выбранные элементы из iterable
c = itertools.count()
lst = list(itertools.islice(c, 10))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

c = itertools.count()
lst = list(itertools.islice(c, 4, 20, 2))
print(lst) # [4, 6, 8, 10, 12, 14, 16, 18]


# -= операции с итераторами =-

# Перестановки
# itertools.permutations(iterable, r=None)
# Возвращает список последовательностей из перестановок по r элементов 
# из исходной последовательности
lst = list(itertools.permutations(['a','b','c']))
print(lst) # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

# Комбинации
# itertools.combinations(iterable, r)
# возвращает список последовательностей по r элементов из исходной
lst = list(itertools.combinations('abc', 2))
print(lst) # [('a', 'b'), ('a', 'c'), ('b', 'c')]
lst = list(itertools.combinations(['1','2','3','4'], 3))
print(lst) #[('1', '2', '3'), ('1', '2', '4'), ('1', '3', '4'), ('2', '3', '4')]

# Группировка
# itertools.groupby(iterable, key=None)
# создает итератор, возвращающий последовательность ключей и групп элементов
# из итератора. Последовательно перебирает итератор и создает новую группу 
# каждый раз при изменении элемента. Возвращаемая группа сама является итератором
lst = [k for k, g in itertools.groupby('AAAABBBCCDAABBB')]
print(lst) # ['A', 'B', 'C', 'D', 'A', 'B']


# itertools.chain(*iterables)
# создает итератор, возвращающий последовательно элементы 
# из каждого переданного итератора:
def gen():
    import random
    for i in range(random.randint(10,20)):
        yield i

for i in itertools.chain([1, 2, 3], ['a', 'b', 'c'], gen()):
    print (i, end=" | ")
print()


# Произведение
# itertools.product(*iterables, repeat=1)
# Возвращает декартово произведение входящих итераторов
lst = itertools.product('ABCD', 'xy')
print(list(lst)) # [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]

lst = itertools.product(range(2), repeat=3)
print(list(lst)) # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

# product(A, repeat=4) <---> product(A, A, A, A).



