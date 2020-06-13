# Module 8
#   Programming Assignment 11
#     Prob-1.py

# Your code below
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def set_make(self, make):
        self._make = make

    def get_make(self):
        return self._make

    def set_model (self, model):
        self._model = model

    def get_model(self):
        return self._model
    
    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

def TestCar():
    carLot = []
    carLot.append(Car("lamborghini:","Aventador:","2001"))
    carLot.append(Car('Ford:', "Mustang:", "2008"))
    carLot.append(Car('chevy:', "Bolt:", "2005"))
    carLot.append(Car('Honda:', "Accord:", "2011"))
    carLot.append(Car('Ford:', "Focus:", "2009"))
    
    for element in carLot:
        print(element.get_make(),element.get_model(),element.get_year())

    for car in carLot:
        print()
        make = input("enter make:")
        car.set_make(make)
        
        model = input("enter model:")
        car.set_model(model)
     
        year = input("enter year:")
        car.set_year(year)
    
    for element in carLot:
        print(element.get_make(),element.get_model(),element.get_year())
        
    

if __name__ == "__main__":
    TestCar()
    



