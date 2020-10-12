class Repair:
    def pop(self):
        return 1
    # def __init__(self,radius):
    #     self.radiusOne = radius

class Driver:
    @staticmethod
    def drive():
        return 'Driving'

class Door:
    def __init__(self,size):
        self.sizeOne = size


class Car(Door,Repair):
    def __init__(self, size, Engine):
        super(Car, self).__init__(size)


car = Car(100)
print(car)
print(car.pop())