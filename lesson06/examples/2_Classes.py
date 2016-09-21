# =================================
#       Основы ООП
# =================================

# class - шаблон для создания объектов
# Классы содержат атрибуты - данные, и методы - функции для обработки данных
class Student:
    # функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)
    def __init__(self, name, surname, birth_date, school, class_room):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school
        self.class_room = class_room

    # метод
    def next_class(self):
        self.class_room = str(int(self.class_room.split()[0]) + 1) + ' ' +\
                          self.class_room.split()[1]

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


# Создаем объекты (экземпляры класса) на основании класса-шаблона
# Агрументы передаются в функцию-конструктор
student1 = Student("Александр", "Иванов", '10.11.1998', "8 гимназия", "5 А")
student2 = Student("Петр", "Сидоров", '10.01.1995', "8 гимназия", "8 Б")

# Выводим текущий класс первого ученика
print(student1.class_room)
# Вызываем метод, который переводит ученика в следующий класс
student1.next_class()
# Проверяем, изменился ли класс
print(student1.class_room)

# Выводим текущий класс второго ученика. Классы имеют общую структуру и методы, но различные данные.
print(student1.class_room)

# Вызываем метод для получения полного отображаемого имени студента
print(student1.get_full_name())
print(student2.get_full_name())

# Можно изменить значение любого атрибута, присвоив ему новое значение
student1.name = 'Вася'
print(student1.name)

# Любой ООП-язык должен следовать следующим парадигмам:
# 1. Инкапсуляция
# 2. Полиморфизм
# 3. Наследование
