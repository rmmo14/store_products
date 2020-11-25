import store_class
import product_class

liquor = store_class.Store(name = "likor store")
prod1 = product_class.Product(name = "apple", price = .6, category = "fruit")
prod2 = product_class.Product(name = "gen soda", price = 1.0, category = "bevarage")
liquor.add_product(new_product = prod1)
liquor.add_product(new_product = prod2)
# print(liquor.list_products)
# liquor.sell_product(id=1)
# print(liquor.list_products)
# liquor.inflation(percent_increase=5)
# print(liquor.list_products)
liquor.set_clearance(category = "bevarage", percent_discount = 60)


# print(liquor.list_products)
# prod1.update_price(percent_change = 100, is_increased = True).print_info()