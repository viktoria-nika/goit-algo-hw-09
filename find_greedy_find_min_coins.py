
# Жадібний алгоритм

def find_coins_greedy(amount):
    denominations = [50, 20, 10, 5, 2, 1] # Номінали монет
    result = {}
    
    for coin in denominations:
        if amount >= coin:
            count = amount // coin # Кількість монет номіналу
            amount -= count * coin # Віднімемо суму монет від загальної суми
            result[coin] = count
            
    return result

amount = 999
greedy_result = find_coins_greedy(amount)
print("Жадібний алгоритм:", greedy_result) 


# Динамічне програмування

def find_min_coins(amount):
    denominations = [1, 2, 5, 10, 20, 50] # Номінали монет
    dp = [float('inf')] * (amount + 1) # Масив для зберігання мінімальної кількості монет
    dp[0] = 0 # Нульова сума вимагає 0 монет
    coin_used = [0] * (amount + 1) # Для зберігання номіналів монет
    
    for coin in denominations:
        for x in range(coin, amount + 1): # Якщо нова комбінація менш ефективна
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {} # Формуємо результат з монет
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
        
    return result

min_coins_result = find_min_coins(amount)
print("Динамічне програмування:", min_coins_result) 
