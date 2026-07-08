class Products:
    
    def __init__(self, product_id, name, count, cost):
        
        self.product_id = product_id
        self.name = name
        self.count = count
        self.cost = cost
        
    def show_product(self):
        print(f'=====\nПродукт: {self.name}\nЦена: {self.cost}\nКоличество: {self.count}\n=====')