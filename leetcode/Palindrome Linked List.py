"""
Palindrome Linked List - Проверка, является ли связный список палиндромом

Алгоритм решения:
1. Проходим по списку и сохраняем все значения в стек
2. Проходим по списку второй раз, сравнивая значения с вершиной стека
3. Если значения совпадают, удаляем элемент из стека
4. Если значения не совпадают, список не является палиндромом
5. Если в конце стек пуст, список является палиндромом
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        
        # Сохраняем все значения в стек
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        
        # Сравниваем значения с вершиной стека
        current = head
        while current:
            if current.val != stack[-1]:
                return False
            stack.pop()
            current = current.next
        
        return len(stack) == 0

