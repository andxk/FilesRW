from pprint import pprint


def read_recipes (file_name):
    '''Чтение файла с рецептами. Результат в виде словаря'''
    res = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            # Формируем список словарей для одного блюда и добавляем в общий словарь
            dish_name = line.strip()
            if dish_name:
                res[dish_name] = []
                ing_cnt = int(file.readline().strip())
                for i in range(ing_cnt):  # Проходим по каждому ингредиенту
                    line = file.readline().strip().split(' | ')
                    # ing = dict(zip(['ingredient_name','quantity','measure'], line))
                    ing = dict(zip(['ingredient_name','quantity','measure'],\
                                   [line[0], int(line[1]), line[2]]))
                    res[dish_name].append(ing)
    return res



def get_shop_list_by_dishes(dishes, person_count):
    '''Суммарный список ингредиентов в зав. от блюд и числа персон '''
    cook_book = read_recipes('recipes.txt')
    res = {}
    for dish in dishes:
        if dish in cook_book:
            ing_list = cook_book.get(dish)
            for ing in ing_list:
                ing_name = ing['ingredient_name']
                ing_quant = ing['quantity'] * person_count
                res.setdefault(ing_name, {'measure':ing['measure'], 'quantity':0})
                ing_val = res[ing_name]
                ing_val['quantity'] += ing_quant
    return res



def get_file_len(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for line in file )
    


def sort_files():
    '''Сортировка списка файлов по числу строк и запись результата в файл "out.txt"'''
    file_dir = 'sorted\\'
    files = ['1.txt', '2.txt', '3.txt']
    flen = [get_file_len(file_dir+fname) for fname in files]
    files = list(zip(files, flen))
    files.sort(key = lambda x: x[1])
    print('Sorted: ', files)

    with open('out.txt', 'w', encoding='utf-8') as outfile:
        for fname, len in files:
            with open(file_dir+fname, 'r', encoding='utf-8') as infile:
                text = infile.readlines()
                text[-1] = text[-1].rstrip() + '\n'  # Не все части текста имеют перенос в конце строки
            outfile.write(f'{fname}\n{len}\n')
            outfile.writelines(text)
    print('Файл "out.txt" сформирован')



pprint(read_recipes('recipes.txt'), width=60)
print()
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
print()

sort_files()
print()
