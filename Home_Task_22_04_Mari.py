import json

# # Задача №1
# # Получение словаря заданного формата


with open('recipes.txt') as f:
  cook_book = {}
  for line in f:
    dish = line.strip()
    ingridients_number = int(f.readline().strip())
    ingridient_list = []
    ingridient_dict = {}
    while ingridients_number:
      ingridient_line = f.readline().strip()
      ingridient = ingridient_line.split(' | ')
      ingridient_dict = {'ingridient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
      ingridient_list.append(ingridient_dict)
      ingridients_number -= 1
    cook_book[dish] = ingridient_list
    f.readline()
  print(json.dumps(cook_book, ensure_ascii=False, indent=2))


# Задача №2
# Получение словаря с названиями ингредиентов и их количества для приготовления блюд


def get_shop_list_by_dishes(dishes, person_count):
  grocery_dict = {}
  ingridient_list = {}
  if ', ' in dishes:
    dishes_list = dishes.split(', ')
  else: dishes_list = [dishes]
  with open('CookBook.txt') as f:
    for line in f:
      for dish in dishes_list:
        if dish in line.strip():
          ingridients_number = int(f.readline().strip())
          while ingridients_number:
            ingridient_line = f.readline().strip()
            ingridient = ingridient_line.split(' | ')
            ingridient[1] = int(ingridient[1]) * int(person_count)
            if ingridient[0] in ingridient_list.keys():
               ingridient[1] = ingridient[1] + ingridient_list[ingridient[0]]
               ingridient_list[ingridient[0]] = ingridient_list[ingridient[0]] + ingridient[1]
            ingridient_list[ingridient[0]] = ingridient[1]
            quantity_dict = {'measure': ingridient[2], 'quantity': ingridient[1]}
            grocery_dict[ingridient[0]] = quantity_dict
            ingridients_number -= 1
          f.readline()
  return grocery_dict
# print(json.dumps(grocery_dict, ensure_ascii=False, indent=1))


def main():
  while True:
    dish_user_input = input('Введите блюда, которые нужно приготовить: ')
    if dish_user_input == 'q':
      print('До свидания')
      break
    person_user_input = input('Введите количество человек: ')
    if dish_user_input == 'q':
      print('До свидания')
      break
    d = {}
    if get_shop_list_by_dishes(dish_user_input, person_user_input) != d:
      print(json.dumps(get_shop_list_by_dishes(dish_user_input, person_user_input), ensure_ascii=False, indent=1))
    elif get_shop_list_by_dishes(dish_user_input, person_user_input) == d:
      print('По вашему запросу ничего не найдено')


main()