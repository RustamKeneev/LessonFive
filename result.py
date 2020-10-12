from anymals import Animals, FishType, Amphibians, Reptiles, Mammals
from anymals import IncapsulateAnymals
from  anymals import IncapsulateAnymalsOne
from anymals import IncapsulateAnymalsTwo
from anymals import IncapsulateAnymalsThree

#Создание объекта и заполнение параметров
fish = FishType("Siga","Fish",1000,"KG")
fish.swim()
print(fish)
print("")

amfibia = Amphibians("Frog","Amphibia",10,"RU")
amfibia.jump()
print(amfibia)
print("")

reptiles = Reptiles("Hameleon","Reptilies",20,"Africa")
reptiles.reptiles()
print(reptiles)
print("")

mammals = Mammals("Panda","Mammals",50,"China")
mammals.mammals()
print(mammals)

print("")

incapsulate = IncapsulateAnymals("Animals")
incapsulate.print_info()
incapsulate1 = IncapsulateAnymals("Animals")
incapsulate1.result = 100
incapsulate1.print_info()

print("")

#Инкапсуляция с защишенным переменной
incapsulate2 = IncapsulateAnymalsOne("AnymalsOne")
incapsulate2.print_info_one()
incapsulate3 = IncapsulateAnymalsOne("AnimalsOne")
incapsulate3._result1 = 40
incapsulate3.print_info_one()

#Инкапсуляция с приватным переменной
incapsulate4 = IncapsulateAnymalsTwo("AnymalsTwo")
incapsulate4.print_info_two()
incapsulate5 = IncapsulateAnymalsTwo("AnymalsTwo")
print(incapsulate5._IncapsulateAnymalsTwo__result)
incapsulate5.print_info_two()

print("")
#Getters
print("Результат геттера: ",incapsulate5.get_result())

print("")

#Setters
print("Результат сеттера")
incapsulate5.set_result(500)
incapsulate5.print_info_two()


print("")

incapsulate6 = IncapsulateAnymalsThree("AnymalsThree")
print("Decarate results ",incapsulate6.results_decorate)


