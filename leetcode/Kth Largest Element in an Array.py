"""
Kth Largest Element in an Array - K-й наибольший элемент в массиве

Алгоритм решения:
1. Используем сортировку подсчетом для эффективной работы с ограниченным диапазоном значений
2. Создаем массив счетчиков размером 2 * shift + 1, где shift = 10^4
3. Подсчитываем частоту каждого элемента, сдвигая индексы на shift
4. Проходим по массиву счетчиков справа налево (от больших к меньшим)
5. Накапливаем сумму частот до тех пор, пока не достигнем k
6. Возвращаем элемент, соответствующий найденной позиции (с учетом сдвига)
"""

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        shift = 10 ** 4
        count_array = [0] * (2 * shift + 1)
        
        # Подсчитываем частоту каждого элемента
        for num in nums:
            count_array[num + shift] += 1
        
        # Ищем k-й наибольший элемент
        cumulative_count = 0
        for i in range(len(count_array) - 1, -1, -1):
            if cumulative_count + count_array[i] >= k:
                return i - shift
            cumulative_count += count_array[i]