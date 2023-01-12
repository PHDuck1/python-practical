class MotorCycle:

    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.dict = obj.__dict__
        self.adapter_methods = adapted_methods
        self.adapter_methods.update(obj.__dict__)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        value = self.adapter_methods.get(attr, 0)
        if value:
            return value
        else:
            return self.__dict__[attr]

    def original_dict(self):
        """Print original object dict"""
        return self.dict

