# coding: utf-8

# class BaseClass():
    # x = 1
    # y = 2

    
# class ChildClass(BaseClass):
    # x = 111
    # y = 222
    
    # def mix(BaseClass):
        # return BaseClass.y
        
        
# c = ChildClass()
# print(c.mix())        

# x = 13
# def func():
    # x = 1
    # class c:
        # x = 2
        # print(x)
        # y = input('y = ')
        
        # def m(self):
            # print(x)
    # i = c()
    # i.m()        
        
# print(x)
# func()

class Bibika:
    def __init__(self, wheels, shassi, engine):
        self.shassi = shassi
        self.wheels = wheels
        self.engine = engine
        self._is_moving = False
        
    def drive(self):
        self._is_moving = True
        print('Еду далеко. Мотор работает: {}'.format(self.engine))
        
    def stop(self):
        self._is_moving = False
    
    def repair_engine(self, engine):
        if not self._is_moving:
            print('Замена двигателя')
        else:
            print('Остановитесь для замены двигателя')
        




