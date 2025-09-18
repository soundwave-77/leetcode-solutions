"""
Substrings of Size Three with Distinct Characters - Подстроки размера три с различными символами

Алгоритм решения:
1. Проходим по строке, рассматривая все подстроки длины 3
2. Для каждой подстроки проверяем, что все три символа различны
3. Если все символы различны, увеличиваем счетчик
4. Возвращаем общее количество "хороших" подстрок
"""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        count = 0
        for i in range(2, len(s)):
            # Проверяем, что все три символа различны
            if s[i-2] != s[i-1] and s[i-1] != s[i] and s[i-2] != s[i]:
                count += 1
        
        return count