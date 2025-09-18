
"""
Longest Substring Without Repeating Characters - Длина самой длинной подстроки без повторяющихся символов

Алгоритм решения:
1. Используем словарь для хранения последней позиции каждого символа
2. Используем указатель cur_pointer для начала текущей подстроки
3. Проходим по строке с помощью указателя i
4. Если символ не встречался или встречался до cur_pointer:
   - Обновляем позицию символа в словаре
   - Обновляем максимальную длину
5. Если символ уже встречался после cur_pointer:
   - Удаляем все символы от cur_pointer до предыдущей позиции этого символа
   - Обновляем cur_pointer на позицию после предыдущего вхождения
   - Обновляем позицию текущего символа
6. Возвращаем максимальную найденную длину
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_positions = {}
        start = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char not in char_positions or char_positions[char] < start:
                char_positions[char] = i
                max_length = max(max_length, i - start + 1)
            else:
                # Удаляем символы от start до предыдущей позиции текущего символа
                for j in range(start, char_positions[char]):
                    char_positions.pop(s[j], None)
                start = char_positions[char] + 1
                char_positions[char] = i
        
        return max_length
