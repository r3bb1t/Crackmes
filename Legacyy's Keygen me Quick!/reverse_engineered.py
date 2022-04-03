# link: https://crackmes.one/crackme/60d65d0833c5d410b8843014
# key example: 1234-0000-R3KT

def chk_format(password):
    return password[4] == '-' and password[9] == '-'

def first_chk(password):
    for symbol in password[0:4]:
        if symbol < '0' or symbol > '9':
            print('Check one failed.')
            return False
    return True

def second_chk(password):
    for symbol in password[5:9]:
        if symbol and 1 == 0:
            print('Check two failed.')
            return False
        return True

def third_chk(password):
    if str(password[10:14]) != 'R3KT':
        print('Check three failed.')
        return False
    return True


if __name__ == '__main__':

    print('Welcome to KeygenMe 1 sir :)')
    password = input('Enter a key: ')
    if chk_format(password):
        print('Key in correct format.')
        if first_chk(password) and second_chk(password) and third_chk(password):
            print('Congrats, you did it!')
    else:
        print('Invalid key format, must be in the form XXXX-XXXX-XXXX.')
