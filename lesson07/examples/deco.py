# coding: utf-8

def log(func):

    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        print('{}({},{}) = {}'.format(func.__name__, args, kwargs, res))
        return res
        
    return decorated    


@log
def my_sum(a, b):
    res = a + b
    return res
    
my_sum = log(my_sum)    
    
# print(my_sum(5,7))    
my_sum(5,7)