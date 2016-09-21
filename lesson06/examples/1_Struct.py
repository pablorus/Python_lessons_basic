# =================================
#    Словарь как структура данных
# =================================

# Словарь по принципу работы похож на объект - по ключу вы находите значение
student = {
    "name": "Алексадр",
    "surname": "Иванов",
    "birth_date": '10.11.1998',
    "school": "8 гимназия",
    "class_room": "5 А"
}
student2 = {
    "name": "Алексадр",
    "surname": "Иванов",
    "birth_date": '10.11.1998',
    "school": "8 гимназия",
    "class_room": "5 А"
}

# Но когда необходимо выполнить какое-то общее действие с данными,
# то функция не очень удобное решение
def next_class(current_class):
    return str(int(current_class.split()[0]) + 1) + \
           ' ' + current_class.split()[1]

# Т.к. кол-во функций постоянно увеличивается
def change_class(current_class):
    pass


student["class_room"] = next_class(student['class_room'])
student2["class_room"] = next_class(student['class_room'])

# Гораздо удобнее работать со сгрупироваными структурами данных с помощью классов...