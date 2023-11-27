
class Asset:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def calculate_depreciation(self):
        pass  # To be implemented in subclasses


class Car(Asset):
    def __init__(self, name, value, model):
        super().__init__(name, value)
        self.model = model

    def calculate_depreciation(self):
        return self.value * 0.1  # Example: Car depreciates by 10%


class RealEstate(Asset):
    def __init__(self, name, value, location):
        super().__init__(name, value)
        self.location = location

    def calculate_depreciation(self):
        return self.value * 0.05  # Example: Real estate depreciates by 5%


# Example usage
car_asset = Car("Luxury Car", 50000, "XYZ Model")
real_estate_asset = RealEstate("City Apartment", 200000, "Downtown")

# Polymorphism - calling the same method on different types
car_depreciation = car_asset