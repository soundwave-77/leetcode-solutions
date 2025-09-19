"""
Remove Duplicates from Sorted Array II - Удаление дубликатов из отсортированного массива (максимум 2 копии)

Алгоритм решения:
1. Используем два указателя: один для чтения, один для записи
2. Отслеживаем текущий элемент и количество его вхождений
3. Если элемент встречается более 2 раз, пропускаем лишние копии
4. Записываем в массив только первые 2 вхождения каждого элемента
5. Возвращаем новую длину массива
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        write_index = 0
        current_num = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == current_num:
                count += 1
                if count <= 2:
                    write_index += 1
                    nums[write_index] = nums[i]
            else:
                current_num = nums[i]
                count = 1
                write_index += 1
                nums[write_index] = nums[i]
        
        return write_index + 1