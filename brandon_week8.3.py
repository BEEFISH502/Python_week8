#3) Password Retry (Max Attempts)
password = 'Secret!'


def login():
    attempts = 0
    while attempts < 3:
        attempt = input('Enter password: ')
        if attempt == password:
            print(f'Access granted.')
            break
        if attempt != password and attempts < 3:
            attempts += 1
            print(f'Incorrect.')
            if attempts >= 3 and attempt != password:
                print(f'Access denied (too many attempts).')

login()