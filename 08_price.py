price = 100
discount = 5

price_with_discount = price - price * discount / 100

print(price_with_discount)

def get_summ(one, two, delimeter='&'):
    return f'{one}{delimeter}{two}'
one = 'Learn'
two = 'python'
res = get_summ(one, two)
print(res.upper())

def format_price(price):
    price = int(price)
    return f'Price is {price} rub.'
my_str = format_price(56.24)
print(my_str)