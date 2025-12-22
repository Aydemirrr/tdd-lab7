# filter_utils.py

def filter_list(items, type_name):
    """
    Фильтрует список по указанному типу (PEP8 compliance).
    """
    # Маппинг строкового названия к объекту типа
    types_map = {
        'str': str,
        'int': int
    }

    target_type = types_map.get(type_name)

    # Чтобы корректно отличать int от bool (так как в Python bool — это подтип int)
    if type_name == 'int':
        return [x for x in items if type(x) is int]

    return [x for x in items if isinstance(x, target_type)]
