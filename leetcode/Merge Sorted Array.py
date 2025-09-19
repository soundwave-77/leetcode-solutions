"""
Merge Sorted Array - Объединение двух отсортированных массивов

Алгоритм решения:
1. Используем три указателя: один для конца nums1, один для конца nums2, один для позиции записи
2. Начинаем с конца массивов и двигаемся к началу
3. Сравниваем элементы и записываем больший в конец nums1
4. Сдвигаем соответствующие указатели
5. Если один из массивов закончился, копируем оставшиеся элементы из другого
6. Модифицируем nums1 на месте без возврата значения
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        # Указатели для записи, конца nums1 и конца nums2
        write_pos = len(nums1) - 1
        i = m - 1
        j = n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[write_pos] = nums1[i]
                i -= 1
            else:
                nums1[write_pos] = nums2[j]
                j -= 1
            write_pos -= 1
        
        # Копируем оставшиеся элементы из nums2
        while j >= 0:
            nums1[write_pos] = nums2[j]
            j -= 1
            write_pos -= 1
