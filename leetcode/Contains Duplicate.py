"""
Contains Duplicate - Проверка наличия дубликатов в массиве

Алгоритм решения:
1. Создаем множество для отслеживания уже встреченных чисел
2. Проходим по каждому элементу массива
3. Если элемент уже есть в множестве, возвращаем True (найден дубликат)
4. Иначе добавляем элемент в множество
5. Если прошли весь массив без дубликатов, возвращаем False
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False