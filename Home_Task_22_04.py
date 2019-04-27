from pprint import pprint

cook_book = {}

with open('recipes.txt') as f:
    for line in f:
        name = line.strip()
        if name not in cook_book.keys():
            cook_book[name] = []
        namber_of_ingredients = int(f.readline().strip())
        while namber_of_ingredients != 0:
            ingridient_dict = {}
            ingridient_name = f.readline().strip().split(' | ')

            ingridient_dict['ingridient_name'] = ingridient_name[0]
            ingridient_dict['quantity'] = ingridient_name[1]
            ingridient_dict['measure'] = ingridient_name[2]

            cook_book[name].append(ingridient_dict)
            namber_of_ingredients -= 1

        f.readline()

    print('Задача 1. Результат: ', cook_book)
    print('Задача 2')

    dishes_input = list(input('Введите блюдо(Омлет, Утка по-пекински, Запеченный картофель, Фахитос): ').split(', '))
    person_count_input = int(input('Введите колличесво персон: '))

    def get_shop_list_by_dishes(dishes, person_count):
        get_shop = {}
        for dish in dishes:

            if dish in cook_book.keys():
                ingridients = cook_book[dish]

            for ingridient in ingridients:
                if ingridient['ingridient_name'] not in get_shop.keys():
                    get_shop[ingridient['ingridient_name']] = {'measure': ingridient['measure'],
                                                               'quantity': int(ingridient['quantity']) * person_count}
                else:
                    old_quantity = get_shop[ingridient['ingridient_name']].pop('quantity')
                    get_shop[ingridient['ingridient_name']] = {'measure': ingridient['measure'], 'quantity': int(
                        ingridient['quantity']) * person_count + old_quantity}

        pprint(get_shop)


    get_shop_list_by_dishes(dishes=dishes_input, person_count=person_count_input)