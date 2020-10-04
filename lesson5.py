class Engine:
    def __init__(self,name,hp):
        self.nameEngine = name
        self.hoursPower = hp

class Wheels:
    def __init__(self,radius):
        self.radiusWheels = radius

class Electronics:
    def __init__(self,country):
        self.countryElectronics = country

class Car:
    def __init__(self, color,brand,price,data_of_production, engine,wheels,electronics):
        self.color1 = color
        self.brand1 = brand
        self.price1 = price
        if isinstance(price,int):
            self.data = data_of_production
        else:
            raise ValueError("Price is not integer")
        self.carEngine = engine
        self.carWheels = wheels
        self.carElectronics = electronics

    def ride(self):
        return "Im driving"

    def __str__(self):
        return f"{self.color1},{self.brand1},{self.price1},{self.data}" + \
                f"{self.carWheels.radiusWheels},{self.carEngine.hoursPower},{self.carElectronics.countryElectronics}"


#Наследование
class Sedan(Car):
    def __init__(self,color,brand,price,data_of_production, engine,wheels,electronics,passenger_places,sedan_type):
        super(Sedan,self).__init__(color,brand,price,data_of_production, engine,wheels,electronics)
        self.passengerPlaces = passenger_places
        self.sedanType = sedan_type


    def __str__(self):
        return f"{super(Sedan,self).__str__()},{self.sedanType},{self.passengerPlaces}"


    def __add__(self, other):
        return f"${self.passengerPlaces + other.passengerPlaces}"


    #
    # def info(self):
    #     super(Car, self).info()
    #     print(f"{self.sedanType},{self.passengerPlaces}")
        # print(f"{self.color1}, {self.brand1}, {self.price1}, {self.data}, {self.ride()}")
        # print(f"{self.carWheels.radiusWheels},{self.carEngine.hoursPower},{self.carElectronics.countryElectronics}")




engine1 = Engine("cool engine",750)
hoursWheels = Wheels(50)
electr = Electronics("Japan")

#
# audi = Car("purple","Audi",12000,"01.10.2020",engine1,hoursWheels,electr)
# audi.info()
#
# car2 = Car("Red","Ferrary",120000,"01.10.2020",engine1,hoursWheels,electr)
# car2.info()


sedan = Sedan("purple","Sedan",12000,"01.10.2020",engine1,hoursWheels,electr,4,"sport")
sedan1 = Sedan("purple","Sedan",12000,"01.10.2020",engine1,hoursWheels,electr,4,"sport")
total = sedan + sedan1
print(total)


