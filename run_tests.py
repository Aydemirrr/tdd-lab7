import sys
sys.path.append('.')

from test_filter import *

def run_all_tests():
    # Тест 1: фильтрация строк
    result1 = filter_list([1, "apple", 2, "banana", 3.5], "str")
    print(f"Test 1 (filter strings): {'PASS' if result1 == ['apple', 'banana'] else 'FAIL'}")
    print(f"  Expected: {['apple', 'banana']}")
    print(f"  Got: {result1}")
    
    # Тест 2: фильтрация чисел
    result2 = filter_list([1, "apple", 2, "banana", 3], "int")
    print(f"\nTest 2 (filter ints): {'PASS' if result2 == [1, 2, 3] else 'FAIL'}")
    print(f"  Expected: {[1, 2, 3]}")
    print(f"  Got: {result2}")
    
    # Тест 3: пустой список
    result3 = filter_list([], "str")
    print(f"\nTest 3 (empty list): {'PASS' if result3 == [] else 'FAIL'}")
    print(f"  Expected: {[]}")
    print(f"  Got: {result3}")
    
    # Тест 4: нет совпадений
    result4 = filter_list([1, 2, 3], "str")
    print(f"\nTest 4 (no matches): {'PASS' if result4 == [] else 'FAIL'}")
    print(f"  Expected: {[]}")
    print(f"  Got: {result4}")
    
    # Тест 5: проверка на bool (дополнительный тест)
    result5 = filter_list([True, False, 1, 0, "text"], "int")
    print(f"\nTest 5 (exclude bool): {'PASS' if result5 == [1, 0] else 'FAIL'}")
    print(f"  Expected: {[1, 0]}")
    print(f"  Got: {result5}")

if __name__ == "__main__":
    run_all_tests()
