#4) Menu Choice Until Valid
def menu():
    while True:
        choice = int(input('Enter a menu choice (1-3): '))
        if choice >= 1 and choice <= 3:
            print(f'You selected option {choice}.')
            break
        else:
            print(f'Invalid choice. Try again.')
menu()