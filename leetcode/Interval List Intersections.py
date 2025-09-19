"""
Interval List Intersections - Пересечения интервалов

Алгоритм решения:
1. Используем два указателя для прохода по обоим спискам интервалов
2. Для каждой пары интервалов проверяем, есть ли пересечение:
   - Интервалы пересекаются, если max(start1, start2) <= min(end1, end2)
3. Если есть пересечение, добавляем его в результат:
   - Начало пересечения: max(start1, start2)
   - Конец пересечения: min(end1, end2)
4. Перемещаем указатель того списка, у которого интервал заканчивается раньше
5. Продолжаем до тех пор, пока не пройдем все интервалы в одном из списков
"""

class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = j = 0
        result = []
        
        while i < len(firstList) and j < len(secondList):
            # Находим пересечение интервалов
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            # Если есть пересечение, добавляем его
            if start <= end:
                result.append([start, end])
            
            # Перемещаем указатель того списка, у которого интервал заканчивается раньше
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return result