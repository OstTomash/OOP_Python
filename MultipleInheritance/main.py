class Vehicle:
    """
    A class representing a generic vehicle.

    Attributes:
        make (str): The make of the vehicle.
        model (str): The model of the vehicle.

    Methods:
        get_info: Returns a string containing the make and model of the vehicle.
    """
    def __init__(self, make, model):
        """
        Initializes a new instance of Vehicle.

        Parameters:
            make (str): The make of the vehicle.
            model (str): The model of the vehicle.
        """
        self.make = make
        self.model = model

    def get_info(self):
        """
        Returns a formatted string representing the make and model of the vehicle.

        Returns:
            str: A string containing the make and model of the vehicle.
        """
        return f'{self.make} {self.model}'


class Electric:
    """
    A class representing a electric vehicle.

    Attributes:
        battery (int): battery level.

    Methods:
        charge: Set battery level to 100
    """
    def __init__(self, battery):
        """
        Initializes a new instance of Electric.

        Parameters:
            battery (int): battery level.
        """
        self.__battery = battery

    def charge(self):
        """
        Set a value of 100 to the battery

        Returns:
            None
        """
        self.__battery = 100


class Car(Vehicle):
    """
    A class representing a car, which is a type of vehicle.

    Attributes:
        wheels (int): The number of wheels the car has.

    Methods:
        get_info: Returns a string containing the make, model, and number of wheels of the car.
    """
    def __init__(self, make, model, wheels):
        """
        Initializes a new instance of Car.

        Parameters:
            make (str): The make of the car.
            model (str): The model of the car.
            wheels (int): The number of wheels the car has.
        """
        super().__init__(make, model)
        self.wheels = wheels

    def get_info(self):
        """
        Returns a formatted string representing the make, model, and number of wheels of the car.

        Returns:
            str: A string containing the make, model, and number of wheels of the car.
        """
        parent_info = super().get_info()
        return f'{parent_info} with {self.wheels} wheels'


class Moto(Vehicle):
    """
    A class representing a motorcycle, which is a type of vehicle.

    Attributes:
        wheels (int): The number of wheels the motorcycle has.

    Methods:
        get_info: Returns a string containing the make, model,
                  and number of wheels of the motorcycle.
    """
    def __init__(self, make, model, wheels):
        """
        Initializes a new instance of Moto.

        Parameters:
            make (str): The make of the motorcycle.
            model (str): The model of the motorcycle.
            wheels (int): The number of wheels the motorcycle has.
        """
        super().__init__(make, model)
        self.wheels = wheels

    def get_info(self):
        """
        Returns a formatted string representing the make, model,
        and number of wheels of the motorcycle.

        Returns:
            str: A string containing the make, model, and number of wheels of the motorcycle.
        """
        parent_info = super().get_info()
        return f'{parent_info} with {self.wheels} wheels'


class ElectricCar(Vehicle, Electric):
    """
    A class representing a car, which is a type of vehicle and electric.

    Attributes:
        make (str): The make of the motorcycle.
        model (str): The model of the motorcycle.
        battery (int): The number of battery level.
    """
    def __init__(self, make, model, battery):
        super().__init__(make, model)
        Electric.__init__(self, battery)


class ElectricMoto(Vehicle, Electric):
    """
    A class representing a car, which is a type of vehicle and electric.

    Attributes:
        make (str): The make of the motorcycle.
        model (str): The model of the motorcycle.
        battery (int): The number of battery level.
    """
    def __init__(self, make, model, battery):
        super().__init__(make, model)
        Electric.__init__(self, battery)


car = Car('Ford', 'Fusion', 4)
bike = Moto('Honda', 'Extra', 3)
nissan = ElectricCar('Honda', 'Extra', 50)
electro_bike = ElectricMoto('Honda', 'Extra', 25)

for item in [Car, Moto, ElectricCar, ElectricMoto]:
    print(item.mro())
