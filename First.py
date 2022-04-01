from typing import Counter


class CounterClass:
    def __init__(self):
        self.counter =0
    def increase_one(self): 
        self.counter =self.counter+ 1
    def decrease_one(self):
        self.counter = self.counter- 1
    def get_value(self):
        print(self.counter)

obj = CounterClass()
obj.increase_one()
obj.get_value() 
obj.increase_one()
obj.increase_one()
obj.get_value() 
obj.decrease_one()
obj.decrease_one()
obj.get_value() 





