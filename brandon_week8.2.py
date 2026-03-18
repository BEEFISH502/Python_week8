#2) Grocery Items Until “done”
def grocery_list():
    items = []
    count = 0
    while True:
        item = input('Enter a grocery item (type done to stop): ')
        if item != 'done':
            items.append(item)
            count += 1
        if item == 'done':
            break
    print(f'Number of items entered: {count}')

grocery_list()