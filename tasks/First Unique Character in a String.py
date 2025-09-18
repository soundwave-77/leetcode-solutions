"""
First Unique Character in a String - Первый уникальный символ в строке

Алгоритм решения:
1. Используем Counter для подсчета частоты каждого символа в строке
2. Проходим по строке слева направо
3. Для каждого символа проверяем, встречается ли он только один раз
4. Возвращаем индекс первого символа с частотой 1
5. Если такого символа нет, возвращаем -1
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1