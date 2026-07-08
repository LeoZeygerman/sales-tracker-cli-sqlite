from database import add_product, find_by_id
from models import Products

def add_products():
    name = input('Введите название товара: ')
    cost = int(input('Введите стоимость товара: '))
    count = int(input('Введите количество товара: '))
    product = add_product(name,cost,count)
    product.show_product()
    
def find_product():
    product_id = int(input('Введите номер товара: '))
    product = find_by_id(product_id)
    product.show_product()
    
    print('1. Изменить количество.')
    print('2. Изменить цену.')
    choice = int(input('Ваш выбор: '))