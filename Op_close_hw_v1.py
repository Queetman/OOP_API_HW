from pprint import pprint

from pathlib import Path
'''
Необходимо написать программу для кулинарной книги.

Список рецептов должен храниться в отдельном файле в следующем формате:

Название блюда
Количество ингредиентов в блюде
Название ингредиента | Количество | Единица измерения
Название ингредиента | Количество | Единица измерения
'''

# Задача 1 Написать код для чтение из файла и приведения текста в приведенный ниже (cook_book2)

file_path = Path("C:\\Users\\queet\\Dropbox\\Нетология_pyton\\3 ООП и работа с API\\3 Открытие и чтение файла, запись в файл\\ДЗ\\recipes.txt")


# открытие файла
def open_file(file_path):
  arr =[]
  with open(file_path, encoding='utf-8') as f:
    for line in f:
      arr.append(line)
  return arr


# обрабочик входного файла
def get_cook_book(arr):
  
  book ={}

  # получение массива, где каждый элемент массива - это блюдо с его данными
  dishes =[]
  arr2 =[]
  for i  in arr:
    if i!='\n':
      arr2.append(i[:-1])# удаление пробела с конца
    else:
      dishes.append(arr2)
      arr2 =[]



  for dish in dishes:
    dish_name =dish[0]# имя блюда
    

    ingr_arr = []
    
    for i in range(2,len(dish)):
      ingridient_data = dish[i].split('|')
 
      ingridient_name = ingridient_data[0].strip()
      ingridient_count = int(ingridient_data[1].strip())
      ingridient_measures = ingridient_data[2].strip()
      
      ingr_arr.append({'ingredient_name':ingridient_name,
                        'quantity':ingridient_count,
                        'measure':ingridient_measures})

      book[dish_name] = ingr_arr# при добавлении ингридиента, перменная будет полностью перезаписываться.
  return book
 
arr = open_file(file_path)

cook_book = get_cook_book(arr)

cook_book2 = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
  ],
  'Стакан молока':[
     {'ingredient_name': 'Молоко', 'quantity': 300, 'measure': 'мл'}
  ]
  }

# Задание 2 Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить.

def get_shop_list_by_dishes(dishes, person_count):  
    out ={}
    
    for dish in dishes:
        if dish in cook_book:
            
          ingridients = cook_book[dish]
          for ingridient in ingridients:
            name = ingridient['ingredient_name']
            measure = ingridient ['measure']
            quantity = ingridient ['quantity']
                       
            if name in out:
              
              quantity_out = out[name]['quantity']             
              out[name]['quantity'] = quantity_out + quantity*person_count
            
            else:
              m_q = {'measure':measure, 'quantity':quantity*person_count}            
              out[name] = m_q
    return out
  
#pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
