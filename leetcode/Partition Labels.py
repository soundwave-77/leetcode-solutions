"""
Partition Labels - Разбиение строки на метки

Алгоритм решения:
1. Создаем словарь с последними позициями каждого символа в строке
2. Проходим по строке, обновляя максимальную позицию для текущего раздела
3. Если текущая позиция равна максимальной позиции, это конец раздела
4. Добавляем длину раздела в результат и начинаем новый раздел
5. Возвращаем список длин разделов
"""

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # Находим последние позиции каждого символа
        last_positions = {char: i for i, char in enumerate(s)}
        
        result = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            # Обновляем конец текущего раздела
            end = max(end, last_positions[char])
            
            # Если достигли конца раздела
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result