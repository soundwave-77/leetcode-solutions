"""
Invalid Transactions - Недействительные транзакции

Алгоритм решения:
1. Парсим все транзакции и группируем их по имени пользователя
2. Для каждой транзакции проверяем два условия недействительности:
   - Сумма транзакции превышает 1000
   - В течение 60 минут была совершена транзакция в другом городе
3. Используем словарь для быстрого поиска транзакций по имени
4. Для проверки временного условия сравниваем время с другими транзакциями того же пользователя
5. Собираем все недействительные транзакции и возвращаем их
"""

from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        invalid_indices = set()
        user_transactions = defaultdict(list)
        parsed_transactions = []
        
        # Парсим транзакции и группируем по пользователям
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)
            user_transactions[name].append((city, time))
            parsed_transactions.append((name, time, amount, city, i))
        
        # Проверяем каждую транзакцию на недействительность
        for name, time, amount, city, i in parsed_transactions:
            # Проверка суммы
            if amount > 1000:
                invalid_indices.add(i)
                continue
            
            # Проверка временного условия
            for other_city, other_time in user_transactions[name]:
                if other_city != city and abs(time - other_time) <= 60:
                    invalid_indices.add(i)
                    break
        
        return [transactions[i] for i in invalid_indices]
