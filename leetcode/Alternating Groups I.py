"""
Alternating Groups I - Количество чередующихся групп

Алгоритм решения:
1. Проходим по каждому элементу в массиве цветов
2. Для каждого элемента проверяем соседние элементы:
   - Левый сосед: i - 1
   - Правый сосед: (i + 1) % len(colors) (с учетом циклического массива)
3. Элемент считается чередующимся, если:
   - Левый и правый соседи имеют одинаковый цвет
   - И этот цвет отличается от цвета текущего элемента
4. Подсчитываем количество таких элементов
5. Возвращаем общее количество чередующихся групп
"""

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        alternating_count = 0
        
        for i in range(len(colors)):
            left = i - 1
            right = (i + 1) % len(colors)
            
            # Проверяем, является ли текущий элемент чередующимся
            if colors[left] == colors[right] and colors[left] != colors[i]:
                alternating_count += 1
        
        return alternating_count