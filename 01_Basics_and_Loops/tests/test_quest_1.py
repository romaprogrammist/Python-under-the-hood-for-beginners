# Copyright (C) 2025 Roman Maksimov.
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

import unittest
import os
import inspect
import sys
from pathlib import Path 
import runpy 

# --- БЛОК 1: НАДЁЖНЫЙ ИМПОРТ ФУНКЦИИ УЧЕНИКА ---

# Определяем абсолютный путь к файлу решения
SOLUTION_FILE_PATH = Path(__file__).resolve().parent.parent / "Quest_1_My_LEN" / "solution_template.py"

# Проверяем существование файла.
if not SOLUTION_FILE_PATH.exists():
    print(f"FATAL ERROR: Файл решения не найден.")
    print(f"Ожидаемый путь: {SOLUTION_FILE_PATH}")
    sys.exit(1) 

# Запускаем файл решения как скрипт
solution_globals = runpy.run_path(str(SOLUTION_FILE_PATH))

# Получаем функцию my_len из словаря.
try:
    my_len = solution_globals['my_len']
except KeyError:
    print(f"FATAL ERROR: В файле 'solution_template.py' не найдена функция 'my_len'.")
    print("Убедитесь, что вы правильно назвали функцию.")
    sys.exit(1)
    
# ----------------------------------------

# Список слов, которые ЗАПРЕЩЕНО использовать в этом квесте
# Мы временно убрали "len(", чтобы избежать конфликта с именем функции my_len в пустом шаблоне.
FORBIDDEN_WORDS = ["sum(", "max(", "min(", "sorted(", "list(", "tuple(", "dict("]

# --- БЛОК 2: ПРОВЕРКА НА ЖУЛЬНИЧЕСТВО ---

class ForbiddenWordChecker(unittest.TestCase):
    """Класс для проверки на использование запрещенных встроенных функций."""
    
    def test_forbidden_words_not_used(self):
        """Проверяем, что ученик не использовал запрещенные слова."""
        
        source_code = inspect.getsource(my_len).strip()
        
        # --- КРИТИЧЕСКИ ВАЖНОЕ ИЗМЕНЕНИЕ: ИСКЛЮЧЕНИЕ my_len ---
        # Заменяем "my_len" на нейтральное имя, чтобы не было ложного срабатывания
        source_code = source_code.replace("my_len", "safe_name") 
        # -----------------------------------------------------

        for word in FORBIDDEN_WORDS:
            self.assertNotIn(
                word, 
                source_code, 
                f"\n\n🚫 ЖУЛЬНИЧЕСТВО ОБНАРУЖЕНО! Вы использовали запрещенное слово '{word.strip('(')}'."
                f"\nЦель этого квеста — написать эту функцию самостоятельно, используя циклы."
            )

# --- БЛОК 3: ПРОВЕРКА КОРРЕКТНОСТИ ---

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