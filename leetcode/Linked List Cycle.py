"""
Linked List Cycle - Проверка наличия цикла в связном списке

Алгоритм решения (алгоритм Флойда - "черепаха и заяц"):
1. Используем два указателя: медленный (черепаха) и быстрый (заяц)
2. Медленный указатель перемещается на один узел за раз
3. Быстрый указатель перемещается на два узла за раз
4. Если в списке есть цикл, быстрый указатель обязательно догонит медленный
5. Если быстрый указатель достигнет конца списка, цикла нет
6. Возвращаем True, если указатели встретились (есть цикл), иначе False
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False