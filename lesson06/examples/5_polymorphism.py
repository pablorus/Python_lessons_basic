# Полиморфизм - разное поведение одного и того же метода в разных классах.
# Например, мы можем сложить два числа, и можем сложить две строки.
# При этом получим разный результат, так как числа и строки являются разными классами.

print(2 + 4)
print('2' + '4')
print((2, 4)+(2, 4))


class Student:
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

