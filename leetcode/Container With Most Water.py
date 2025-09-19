"""
Container With Most Water - Максимальная площадь контейнера с водой

Алгоритм решения:
1. Используем два указателя: левый (начало) и правый (конец массива)
2. Вычисляем площадь контейнера как min(height[left], height[right]) * (right - left)
3. Обновляем максимальную площадь, если текущая площадь больше
4. Перемещаем указатель с меньшей высотой внутрь (так как площадь ограничена меньшей высотой)
5. Продолжаем до тех пор, пока указатели не встретятся
6. Возвращаем максимальную найденную площадь
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Вычисляем площадь текущего контейнера
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Перемещаем указатель с меньшей высотой
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area