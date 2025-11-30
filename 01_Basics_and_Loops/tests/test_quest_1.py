# 01_Basics_and_Loops/tests/test_quest_1.py

import unittest
import os
import inspect

# Импортируем функцию, которую должен написать ученик
# Мы делаем относительный импорт, чтобы он работал в тестовом окружении
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Quest_1_My_LEN'))
from solution_template import my_len 

# Список слов, которые ЗАПРЕЩЕНО использовать в этом квесте
FORBIDDEN_WORDS = ["len("] 

class ForbiddenWordChecker(unittest.TestCase):
    """Класс для проверки на использование запрещенных функций."""
    
    def test_forbidden_words_not_used(self):
        """Проверяем, что ученик не использовал запрещенные слова (например, len())."""
        
        # Получаем исходный код функции my_len
        source_code = inspect.getsource(my_len)
        
        for word in FORBIDDEN_WORDS:
            # Преобразуем код и слово в нижний регистр для регистронезависимой проверки
            self.assertNotIn(
                word, 
                source_code, 
                f"ЖУЛЬНИЧЕСТВО! Вы использовали запрещенное слово '{word.strip('(')}' в своем решении. "
                f"Цель этого квеста — написать эту функцию самостоятельно!"
            )

class TestMyLenFunction(unittest.TestCase):
    """Тестирование корректности функции my_len."""
    
    def test_my_len_with_list(self):
        """Проверка длины на списке целых чисел."""
        self.assertEqual(my_len([10, 20, 30, 40]), 4)
        self.assertEqual(my_len([]), 0)
        
    def test_my_len_with_string(self):
        """Проверка длины на строке."""
        self.assertEqual(my_len("hello"), 5)
        self.assertEqual(my_len(""), 0)

    def test_my_len_with_tuple(self):
        """Проверка длины на кортеже."""
        self.assertEqual(my_len((1, 2, 3)), 3)
        
    def test_my_len_with_large_list(self):
        """Проверка длины на большом списке."""
        large_list = list(range(100))
        self.assertEqual(my_len(large_list), 100)

if __name__ == '__main__':
    unittest.main()