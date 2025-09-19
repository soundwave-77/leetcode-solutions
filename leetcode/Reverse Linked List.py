"""
Reverse Linked List - Разворот связного списка

Алгоритм решения:
1. Используем три указателя: prev (предыдущий), current (текущий), next (следующий)
2. Инициализируем prev как None
3. Проходим по списку:
   - Сохраняем ссылку на следующий узел
   - Меняем направление связи: current.next = prev
   - Перемещаем указатели: prev = current, current = next
4. Возвращаем prev как новую голову списка
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev