class Product:
    def __init__(self, name:str, price:float, quantity:int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def update_price(self, new_price:float) -> None:
        self.price = new_price
        
    def restock(self, additional_quantity:int) -> None:
        self.quantity = additional_quantity
        
class Inventory:
    def __init__(self) -> None:
        self.products:dict[str, Product] = {}
        
    def add_product(self, product:Product) -> None:
        self.products[product.name] = product
        
    def remove_product(self, product_name:str) -> None:
        del self.products[product_name]