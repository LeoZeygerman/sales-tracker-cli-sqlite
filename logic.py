from database import add_product, find_by_id, new_count, new_cost, show_all_data, delete_product_data
from models import Products

def add_products():
    name = input('Введите название товара: ')
    cost = int(input('Введите стоимость товара: '))
    count = int(input('Введите количество товара: '))
    product = add_product(name,cost,count)
    product.show_product()
    
def find_product():
    try:
        product_id = int(input('Введите номер товара: '))
        product = find_by_id(product_id)
        product.show_product()
        
        print('1. Изменить количество.')
        print('2. Изменить цену.')
        print('3. Назад.')
        choice = int(input('Ваш выбор: '))
        
        if choice == 1:
            new_product_count = int(input('Введите +/- количество товара: '))
            product_count = new_count(product_id, new_product_count)
            product_count.show_product()
            
        elif choice == 2:
            new_product_cost = int(input('Введите +/- цену товара: '))
            product_cost = new_cost(product_id, new_product_cost)
            product_cost.show_product()
            
        elif choice == 3:
            pass
    except UnboundLocalError:
        print('Товара нет!')
        
def show_all():
    products = show_all_data()
    for product in products:
        product.show_product()
        
def delete_product():
    product_id = int(input('Введите ID продукта,который хотите удалить: '))
    delete_product_data(product_id)
    show_all()
    print('Продукт удален!')
    