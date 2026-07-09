from database import create_base
from logic import add_products, find_product, show_all

while True:
    try:
        
        create_base()
        print('===Sales Tracker===')
        print('1. Добавить продукт.')
        print('2. Найти товар.')
        print('3. Список всех товаров.')
        print('4. Удалить товар.')
        print('5. Выйти.')
        choice = int(input('Ваш выбор: '))
        
        if choice == 1:
            add_products()
        elif choice == 2:
            find_product()
        elif choice == 3:
            show_all()
        
    except ValueError:
        print('Ошибка при вводе!')