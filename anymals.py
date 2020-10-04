#Создание конструктора
class ToSwim:
    def __init__(self,distance, country):
        self.toSwimDistance = distance
        self.toSwimCountry = country
#Создание конструктора
class ToRun:
    def __init__(self,distance, country):
        self.toRunDistance = distance
        self.toRunCountry = country

#Создание конструктора
class ToFlying:
    def __init__(self,distance, country):
        self.toFlyingDistance = distance
        self.toFlyingCountry = country

#Создание класса
class Animals:
    def __init__(self, name, type_animal,distance,country):
        self.nameAnimal = name
        self.typeAnimals = type_animal
        if isinstance(distance,int):
            self.distance = distance
        else:
            raise ValueError
        self.country = country

    def __str__(self):
        return f"{self.nameAnimal},{self.typeAnimals},{self.distance},{self.country}"


    def swim(self):
        print("Fish types ->")

    def jump(self):
        print("Amphibians types ->")

    def fly(self):
        print("Birds types ->")

    def reptiles(self):
        print("Reptiles types ->")

    def mammals(self):
        print("Mammals types ->")

#Наследование класса
class FishType(Animals):
    def __init__(self, name,type_animal,distance,country):
        super(FishType, self).__init__(name,type_animal,distance,country)
        self.mDistance = distance
        self.mCountry = country

#Наследование класса
class Amphibians(Animals):
    def __init__(self,name,type_animals,distance,country):
        super(Amphibians, self).__init__(name,type_animals,distance,country)
        self.mDistance = distance
        self.mCountry = country

#Наследование класса
class Birds(Animals):
    def __init__(self, name, type_animals,distance, country):
        super(Birds, self).__init__(name,type_animals,distance,country)
        self.mDistance = distance
        self.mCountry = country

#Наследование класса
class Reptiles(Animals):
    def __init__(self,name,type_animals,distance,country):
        super(Reptiles, self).__init__(name,type_animals,distance,country)
        self.mDistance = distance
        self.mCountry = country

#Наследование класса
class Mammals(Animals):
    def __init__(self,name,type_animals,distance,country):
        super(Mammals, self).__init__(name,type_animals,distance,country)
        self.mDistance = distance
        self.mCountry = country

class IncapsulateAnymals:
    def __init__(self,name):
        self.name = name
        self.result = 20

    def print_info(self):
        print(f"Name: {self.name}, Result:{self.result}")

#Класс с защищенным переменной
class IncapsulateAnymalsOne:
    def __init__(self,name1):
        self.name1 = name1
        self._result1 = 30

    def print_info_one(self):
        print(f"NameOne: {self.name1}, ResultOne: {self._result1}")

#Класс с приватной переменной
class IncapsulateAnymalsTwo:
    def __init__(self,name2):
        self._IncapsulateAnymalsTwo__result = None
        self.nameTwo = name2
        self.__result = 66

    def print_info_two(self):
        print(f"NameTwo: {self.nameTwo}, ResultsTwo : {self.__result}")

    #Геттеры
    def get_result(self):
        return self.__result

    #Cеттеры
    def set_result(self,values):
        if values in range(0,1000000):
            self.__result = values
        else:
            print("Int in mistakes")


class IncapsulateAnymalsThree:
    def __init__(self,names3):
        self._IncapsulateAnymalsThree__result = None
        self.namesThree = names3
        self.__resultsThree = 55

    @property
    def results_decorate(self):
        return self.__resultsThree

    @results_decorate.setter
    def results_decorate(self,valuesOne):
        if valuesOne in range(0,1000000000):
            self.__resultsThree = valuesOne
        else:
            print("Integer make mistakes")

    def print_info_three(self):
        print(f"Namethree : {self.namesThree}, {self.__resultsThree}")
