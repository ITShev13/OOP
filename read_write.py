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


# Задача 2 

   
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


# Задача 3

def all_one_file(folder): # ввести название папки с метом раположения необходимых файлов .txt
    import os
    if os.path.exists(folder): # проверяем существует ли данная папка в каталоге
        carrent = os.getcwd() # узнаем путь к текущей папке
        fool_path = os.path.join(carrent, folder) # полный путь работающий в любой системе к папке с нужными файлами в проекте
        # file_list = os.listdir(fool_path) # список нужных файлов

        os.chdir(fool_path) # перехожу в нужную директорию (с файлами)
        file_list = {}
        for file_name in os.listdir(fool_path):    
            if file_name.endswith('.txt'): # проверяем у данного файла расширение .txt
                with open(file_name, 'rt', encoding='utf-8') as file: # считаем количество строк в файлах .txt
                    len = 0
                    text_list = []
                    for line in file.readlines():
                        len += 1
                        text_list.append(line)
                file_list[file_name] = len, text_list
        # pprint(file_list)

        sort_file_list = sorted(file_list.items(), key=lambda val: val[1]) # сортируем словарь file_list
        # pprint(sort_file_list)

        os.chdir('../') # возвращаеся в директорию уровнем выше (в основную папку проекта) где будем создавать новый файл
        #  в цикле из словаря записать в новый файл
        with open('res.txt', 'w', encoding='utf-8') as res:
            for name_file, nam_lines in sort_file_list:
                res.write(f'{name_file}\n{nam_lines[0]}\n{"".join(nam_lines[1])}\n')
            path_new_file = os.path.abspath("res.txt") # путь до нового файла
            return print(f'Сформированный файл находится в {path_new_file}')
    else:
        return print('В данном каталоге отсутствует указанная папка с файлами')    

all_one_file('неверное имя папки')
all_one_file('zadacha_3')