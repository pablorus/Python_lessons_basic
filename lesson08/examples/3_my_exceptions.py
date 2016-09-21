# Можно, а часто и нужно создавать исключения отличающиеся от стандартных типов
# Любое исключение - это экземпляр класса, который должен наследоваться от Exception
class ShortInputError(Exception):
    """Пользовательский класс исключения."""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        # Добавляем два доп.атрибута, для вывода более информативного сообщения об ошибке
        self.length = length
        self.atleast = atleast

    # Переопределяем, чтобы вывести сообщение, которое нам нужно
    def __str__(self):
        return 'ShortInputException: Длина введённой строки -- {0}; ' \
               'ожидалось, как минимум, {1}'.format(self.length, self.atleast)


class TestError(ShortInputError):
    pass


def max_char(text):
    if len(text) < 2:
        # Вызываем исключение с помощью оператора raise
        raise ShortInputError(len(text), 2)
        # ...


# Перехватываем и обрабатываем свое исключение
try:
    max_char("H")
except ShortInputError as ex:
    print(ex)
else:
    print('Не было исключений.')
finally:
    # Блок finally приведен просто для примера полной структуры перехвата и обработки
    pass
