"""
Best Time to Buy and Sell Stock - Максимальная прибыль от покупки и продажи акций

Алгоритм решения:
1. Инициализируем минимальную цену как первую цену и максимальную прибыль как 0
2. Проходим по всем ценам начиная со второй
3. Если текущая цена меньше минимальной цены, обновляем минимальную цену
4. Иначе вычисляем прибыль от продажи по текущей цене и обновляем максимальную прибыль
5. Возвращаем максимальную прибыль
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit
