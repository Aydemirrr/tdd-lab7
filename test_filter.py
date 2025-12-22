# test_filter.py
import pytest
from filter_utils import filter_list

def test_filter_strings():
    # Тест для фильтрации строк из смешанного списка
    assert filter_list([1, "apple", 2, "banana", 3.5], "str") == ["apple", "banana"]

def test_filter_ints():
    # Тест для фильтрации чисел из смешанного списка
    assert filter_list([1, "apple", 2, "banana", 3], "int") == [1, 2, 3]

def test_empty_list():
    # Тест для пустого списка
    assert filter_list([], "str") == []

def test_no_matches():
    # Тест для списка, не содержащего элементов нужного типа
    assert filter_list([1, 2, 3], "str") == []
