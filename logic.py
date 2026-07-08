from database import add_product
from models import Products

def add_products():
    name = input('Введите название товара: ')
    cost = int(input('Введите стоимость товара: '))
    count = int(input('Введите количество товара: '))
    product = add_product(name,cost,count)
    product.show_product()