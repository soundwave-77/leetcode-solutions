"""
Find the Difference of Two Arrays - Разность двух массивов

Алгоритм решения:
1. Преобразуем оба массива в множества для быстрого поиска
2. Находим элементы, которые есть в nums1, но нет в nums2
3. Находим элементы, которые есть в nums2, но нет в nums1
4. Возвращаем список из двух списков: [разность_1, разность_2]
"""

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Элементы, которые есть в nums1, но нет в nums2
        diff1 = [x for x in set1 if x not in set2]
        # Элементы, которые есть в nums2, но нет в nums1
        diff2 = [x for x in set2 if x not in set1]
        
        return [diff1, diff2]