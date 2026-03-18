#7) Input Validation: Positive Number Only
def positive_num():
    num = int(input('Enter a positive integer: '))
    while num <= -1:
        print(f'Invalid. Try again.')
        num = int(input('Enter a positive integer: '))
    if num >= 0 or num == 0:
        print(f'You entered: {num}')

positive_num()