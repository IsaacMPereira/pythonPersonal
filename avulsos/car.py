class Car:
    def __init__ (self, model, year, for_sale):
        self.model = model
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f"Im driving {self.model}")