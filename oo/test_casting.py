import unittest

class Animal:
    def __init__(self):
        print('initializing animal')
        
class TwoWingedAnimal(Animal):
    def __init__(self):
        print('initializing two-winged animal')
        self.has_wings = True
        
class Predator(Animal):
   def __init__(self):
        print('initializing predator')
        
class Bat(Predator, TwoWingedAnimal):
    count = 0
    def __init__(self):
        self.blood_sucker = True
        self.__class__.count += 1
        super().__init__()
        
    @classmethod
    def increment(cls):
        cls.count += 1