from filter_utils import filter_list

# Демонстрация работы
mixed_list = [1, "hello", 42, "world", True, False, 3.14, "test"]

print("Исходный список:", mixed_list)
print("Только строки:", filter_list(mixed_list, "str"))
print("Только целые числа:", filter_list(mixed_list, "int"))
print("Пустой список:", filter_list([], "str"))
print("Только строки (нет строк):", filter_list([1, 2, 3], "str"))
