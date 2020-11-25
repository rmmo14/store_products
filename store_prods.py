class Store:
    def __init__(self, name, list_products = []):
        if name == "":
            print("name must be provided")
        self.name = name
        self.list_products = []
    def add_product(self, new_product):
        self.added_product = {
            "name" : new_product.name,
            "price" : new_product.price,
            "category" : new_product.category
        }
        # print('added product is:', self.added_product)
        self.list_products.append(self.added_product)
        return self
    def sell_product(self, id):
        self.id = id
        self.list_products.pop(self.id)
        return self
    def inflation(self, percent_increase):
        self.percent_increase = percent_increase/100
        for i in range(0,len(self.list_products)):
            self.list_products[i].price += self.percent_increase*self.list_products[i].price 
        return self
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

liquor = Store(name = "likor store")
prod1 = Product(name = "apple", price = .6, category = "fruit")
prod2 = Product(name = "gen soda", price = 1, category = "bevarage")
liquor.add_product(new_product = prod1)
liquor.add_product(new_product = prod2)
print(liquor.list_products)
liquor.sell_product(id=1)
print(liquor.list_products)
liquor.inflation(percent_increase=5)
print(liquor.list_products)


# print(liquor.list_products)
# prod1.update_price(percent_change = 100, is_increased = True).print_info()
