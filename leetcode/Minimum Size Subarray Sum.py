"""
Subarray Sum Equals K - Количество подмассивов с суммой равной K

Алгоритм решения:
1. Используем хеш-таблицу для хранения частоты префиксных сумм
2. Инициализируем с префиксной суммой 0 (встречается 1 раз)
3. Проходим по массиву, вычисляя текущую префиксную сумму
4. Для каждой префиксной суммы ищем, сколько раз встречалась сумма (current_sum - k)
5. Добавляем найденное количество к результату
6. Обновляем частоту текущей префиксной суммы
7. Возвращаем общее количество подмассивов с суммой k
"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        current_sum = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        result = 0
        
        for num in nums:
            current_sum += num
            target_sum = current_sum - k
            result += prefix_sum_count[target_sum]
            prefix_sum_count[current_sum] += 1
        
        return result