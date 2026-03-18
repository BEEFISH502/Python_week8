#5) Keep Adding Deposits Until 0
def savings():
    total = 0
    while True:
        deposit = float(input('Enter a deposit amount (0 to stop): '))
        if deposit != 0:
            total += deposit
        elif deposit == 0:
            break
    print(f'Total saved: {total:.2f}')
savings()