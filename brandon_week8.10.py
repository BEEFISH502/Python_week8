#10) Simple “Continue? (y/n)” Loop
answer = input('Continue? (y/n): ')
while answer != 'y' and answer != 'n':
    print('Invalid. Enter y or n.')
    answer = input('Continue? (y/n): ')
    if answer == 'y' or answer == 'n':
        print(f'Final choice: {answer}')