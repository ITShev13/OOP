# Задача 1 ("открытие и чтение файла, запись в файл")

from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as recipes:
    cook_book = {}
    for line in recipes:
        dish_name = line.strip() # имя блюда
        namber_ingredient = int(recipes.readline()) # количество ингредиентов в блюде
        ingredients = [] # список ингридиентов в блюде
        for _ in range(namber_ingredient): # выполняем цикл по количеству ингредиентов для их добавления в список
            ingred = recipes.readline()
            ingredient_name, quantity, measure = ingred.strip().split(' | ') # радзедяем ингредиенты и получаем список
            ingredient = {'ingredient_name': ingredient_name,
                          'quantity': quantity,
                          'measure': measure
                          } #создаем словарь из ингредиентов
            ingredients.append(ingredient)
        recipes.readline() # пропускаем (забираем) пустую строку
        cook_book[dish_name] = ingredients # добавляем в словарь ключь (имя блюда) и значение (словарь ингредиентов)
    # pprint(cook_book)
        
# мой первоначальный вариант (недоделанный)
# def get_shop_list_by_dishes(dishes, person_count=1):
#     res = {}
#     for d in dishes:
#         if d in cook_book.items():
#             return print(d)
#             for i, q, m in cook_book[d]:
                
#                 return print(d)
    
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes: # проходим по списку необходимых блюд
        if dish in cook_book: # проверяем есть ли блюдо в книге
            for amount in cook_book[dish]: # берем игнгредиенты блюда
                if amount['ingredient_name'] in result: # если ингридиенты уже есть в листе то необходимо их сложить
                    result[amount['ingredient_name']]['quantity'] += int(amount['quantity']) * person_count
                else: # иначе просто добавляем
                    result[amount['ingredient_name']] = {'measure': amount['measure'],'quantity': int((amount['quantity'])) * person_count}
        else:
            return print('Указанное блюдо отсутсвует в нашей книге')
    return print(result)



get_shop_list_by_dishes(4, ['Омлет', 'Фахитос'])








import os.path
import os

def acounting(file:str) -> int:
    return sum(1 for _ in open('1.txt', 'rt', encoding='utf-8'))

def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r',encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()



file_for_writing = os.path.abspath('\\~GreshniK~\\Обучение в Нетологии\\OOP\\1.txt')
base_path = os.getcwd()
location = os.path.abspath('\\~GreshniK~\\Обучение в Нетологии\\OOP')
rewriting(file_for_writing, base_path, location)