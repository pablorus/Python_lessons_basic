# coding: utf-8

import sys

class BadNumber(Exception):

    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return '! ****  Нехорошее число: {} ****'.format(self.x)
        
        

f = open('numbers.txt')

for line in f:
    try:
        x = int(line.strip())
        if x == 13:
            raise BadNumber(x)
    except ValueError:
        print('Ошибка перевода числа в int')
        sys.exit(13)
    except BadNumber as bn:
        print(bn)
        
    else:
        print(x)
        try:
            y = 1000 / x
        except ZeroDivisionError as z:
            print(z)
        else:    
            print(y)
    finally:
        print('Выходим из блока try')
            
            
