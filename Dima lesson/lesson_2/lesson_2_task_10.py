def bank(x, y):
    rate = 0.10
    for _ in range(y):
        x += x * rate
    return x

deposit = 5000
years = 5
summa = bank(deposit,years)
print(f'Сумма на счету(years) лет будет: {summa} рублей')
