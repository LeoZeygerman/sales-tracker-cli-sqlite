from database import create_base
from logic import add_products

while True:
    try:
        
        create_base()
        print('===Sales Tracker===')
        print('1. Добавить продукт.')
        print('2. Найти товар.')
        print('3. Список всех товаров.')
        print('4. Выйти.')
        choice = int(input('Ваш выбор: '))
        
        if choice == 1:
            add_products()
        
    except ValueError:
        print('Ошибка при вводе!')