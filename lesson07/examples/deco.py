# coding: utf-8
# === Декораторы ===
# Применяются для расширения функционала классов и функций

def log(func):
    def decorated(*args, **kwargs):     # <- функция, которая заменит собой декорируемую функцию
        res = func(*args, **kwargs)     # <- тут происходит вызов декорируемой функции
                                        # а всё остальное - это как раз расширение функционала
        print('{}({},{}) = {}'.format(func.__name__, args, kwargs, res))
        return res
        
    return decorated    


@log        # <- применение декоратора аналогично записи:  my_sum = log(my_sum)  
def my_sum(a, b):
    res = a + b
    return res
    

# print(my_sum(5,7))    
my_sum(5,7)