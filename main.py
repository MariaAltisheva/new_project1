
BREAD_PRICE = 3.49
DISCOUNT_RATE = 0.60

num_loaves = int(input('Введите количество вчерашних буханок хлеба: '))

regulag_price = num_loaves * BREAD_PRICE
discount = regulag_price * DISCOUNT_RATE

total = regulag_price - discount

print('Номинальная цена: %5.2f' % regulag_price)
print('Сумма скидки: %5.2f' % discount)
print(f'Итого: {round(total, 2)}')




