class Animals:
    def __init__(self, name, age):
        self.nameOne = name
        self.ageOne = age

    @property
    def name(self):
        pass

    @name.setter
    def name(self,value):
        if type(value) != str:
            raise ValueError('Имя не является текстом')
        return self._name

    @property
    # Показ данных
    def age(self):
        pass

    @age.setter
    # Получение данных
    def age(self,value):
        if type(value) !=int is not int:
            raise ValueError("Возврат не явлется числом")
        self._age = value


animals = Animals('Barbos',5)
animals.ageOne = 11
animals._name = "New"
if animals.ageOne > 10:
    print('Old animal')

print(animals.ageOne)
print(animals._name)