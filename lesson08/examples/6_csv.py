import csv

# -= Чтение =-

# Создание диалекта
csv.register_dialect('excel-semicolon', delimiter=';')

f = open('employees.csv', 'rt')
try:
    reader = csv.reader(f, dialect="excel-semicolon")
    for row in reader:
        print(row)
finally:
    f.close()

# Авто определение диалекта файла
with open('employees.csv') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    for row in reader:
        print(row)

# Считывание в namedtuple
from collections import namedtuple
Employee = namedtuple('Employee', 'name, age, department, pay')

with open('employees.csv') as csvfile:
    for emp in map(Employee._make, csv.reader(csvfile, dialect)):
        print(emp.name, emp.pay)


# Работа со словарями
# В качестве ключей используется первая строка
with open('employees_excel.csv', encoding='windows-1251') as csvfile:
    reader = csv.DictReader(csvfile, dialect=dialect)
    for row in reader:
        print (row)



# -= Запись =-

encoding = 'windows-1251'
# encoding = 'utf-8'
with open('employees_out.csv', 'w', encoding=encoding) as csvfile:
    writer = csv.writer(csvfile, dialect='excel-semicolon')
    writer.writerow( ('Заголовок 1', 'Заголовок 2', 'Заголовок 3') )
    for i in range(10):
        writer.writerow( ('строка %s' % (i+1), 2**i, '08/%02d/13' % (i+1)) )


# Запись словарей
with open('employees_out.csv', 'w', encoding=encoding) as csvfile:
    fieldnames = ('Заголовок 1', 'Заголовок 2', 'Заголовок 3')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel-semicolon')
    headers = {name:name for name in fieldnames}
    writer.writerow(headers)
    for i in range(10):
        data = dict(zip(fieldnames, ['строка %s' % (i+1), 2**i, '08/%02d/13' % (i+1)]))
        writer.writerow(data)








