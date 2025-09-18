"""
Isomorphic Strings - Проверка изоморфности строк

Алгоритм решения:
1. Проверяем, что длины строк одинаковы
2. Создаем счетчики для подсчета частоты каждого символа в обеих строках
3. Создаем словарь для маппинга символов из первой строки во вторую
4. Проходим по каждой позиции в строках:
   - Если частоты символов на соответствующих позициях не равны, строки не изоморфны
   - Если символ уже замаплен на другой символ, строки не изоморфны
   - Иначе создаем маппинг для текущего символа
5. Если все проверки пройдены, строки изоморфны
"""

from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        char_mapping = {}
        
        for i in range(len(s)):
            # Проверяем, что частоты символов на соответствующих позициях равны
            if s_counter[s[i]] != t_counter[t[i]]:
                return False
            
            # Проверяем, что символ не замаплен на другой символ
            if s[i] in char_mapping and char_mapping[s[i]] != t[i]:
                return False
            
            # Создаем маппинг
            char_mapping[s[i]] = t[i]
        
        return True