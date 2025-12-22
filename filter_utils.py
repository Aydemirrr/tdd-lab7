# filter_utils.py

def filter_list(items, type_name):
    """
    Фильтрует список по указанному типу.
    :param items: Список элементов разных типов
    :param type_name: Строка 'str' или 'int'
    :return: Новый список с элементами только указанного типа
    """
    result = []

    # Определяем, какой тип искать
    target_type = str if type_name == 'str' else int

    for item in items:
        # Проверяем тип элемента (и исключаем bool для int, так как bool — подтип int)
        if type_name == 'int' and isinstance(item, int) and not isinstance(item, bool):
            result.append(item)
        elif type_name == 'str' and isinstance(item, str):
            result.append(item)

    return result
