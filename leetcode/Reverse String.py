"""
Reverse String - Разворот строки на месте

Алгоритм решения:
1. Используем два указателя: левый (начало) и правый (конец массива)
2. Пока левый указатель меньше правого:
   - Меняем местами символы на позициях left и right
   - Сдвигаем левый указатель вправо
   - Сдвигаем правый указатель влево
3. Модифицируем массив на месте без возврата значения
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1