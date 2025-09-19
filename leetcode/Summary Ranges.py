"""
Summary Ranges - Сводка диапазонов

Алгоритм решения:
1. Обрабатываем пустой массив и массив из одного элемента
2. Используем два указателя для отслеживания начала и конца диапазона
3. Проходим по массиву, проверяя разность между соседними элементами
4. Если разность > 1, завершаем текущий диапазон и начинаем новый
5. Для каждого диапазона:
   - Если начало = конец, добавляем только одно число
   - Иначе добавляем диапазон в формате "start->end"
6. Обрабатываем последний диапазон после цикла
"""

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        result = []
        start = 0
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                # Завершаем текущий диапазон
                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        
        # Обрабатываем последний диапазон
        if start == len(nums) - 1:
            result.append(str(nums[start]))
        else:
            result.append(f"{nums[start]}->{nums[-1]}")
        
        return result