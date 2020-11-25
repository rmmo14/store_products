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
        # how can i use the update_price method to do this for all products...
        self.percent_increase = percent_increase/100
        for i in range(0,len(self.list_products)):
            print('before inflation:', self.list_products[i]['price'])
            self.list_products[i]['price'] += self.percent_increase*self.list_products[i]['price']
            print('after inflation:', self.list_products[i]['price'])
        return self
    def set_clearance(self, category, percent_discount):
        # how can i use the update_price method to do this for all products...
        self.category = category
        self.percent_discount = percent_discount/100
        for i in range(0, len(self.list_products)):
            print('before clearance:', self.list_products[i]['price'])
            if self.list_products[i]['category'] == self.category:
                self.list_products[i]['price'] -= self.percent_discount*self.list_products[i]['price']
            print('after clearance:', self.list_products[i]['price'])
        return self