import store_class

class Product:
    def __init__(self, name, price, category):
        if name == "" or price == "" or category == "":
            print("all fields must be provided!")
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        self.percent_change = percent_change/100
        self.is_increased = is_increased
        if is_increased == True:
            self.price += self.price*self.percent_change
            print(self.price)
        else:
            self.price -= self.price*self.percent_change
            print(self.price)
        return self
    def print_info(self):
        print(f"Name of product: {self.name}, category is: {self.category}, price is: $ {self.price}")
        return self

