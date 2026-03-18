#8) Running Total with Quit Word
def totals():
    subtotal = 0
    while True:
        price = input('Enter item price (type quit to finish): ')
        if price == 'quit':
            break
        else:
            subtotal += float(price)
    print(f'Subtotal: {float(subtotal):.2f}')

totals()