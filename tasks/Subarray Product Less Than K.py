"""
Subarray Product Less Than K - Количество подмассивов с произведением меньше K

Алгоритм решения:
1. Используем технику скользящего окна с двумя указателями
2. Если k <= 1, возвращаем 0 (произведение всегда >= 1)
3. Поддерживаем произведение элементов в текущем окне
4. Расширяем окно, добавляя элементы справа
5. Если произведение >= k, сжимаем окно слева
6. Количество подмассивов в текущем окне = right - left + 1
7. Суммируем количество подмассивов для всех валидных окон
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left = 0
        product = 1
        count = 0
        
        for right in range(len(nums)):
            product *= nums[right]
            
            # Сжимаем окно, пока произведение >= k
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
            
            # Добавляем количество подмассивов в текущем окне
            count += right - left + 1
        
        return count