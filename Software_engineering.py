# Diego Curbelo
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    option = input('Please enter an option: ')
    return option


def encode(password):
    password.split()
    new_password = []
    for num in password:
        if int(num) >= 7:
            num = (int(num) + 3) % 10
        else:
            num = int(num) + 3
        new_password.append(str(num))
    new_password = ''.join(new_password)
    print('Your password has been encoded and stored!')
    print('')
    return new_password

def decode(secret):
    password = ""
    for i in secret:
        each_dig_password = (int(i) - 3) % 10
        password += str(each_dig_password)
    return password

option = '0'
while option != '3':
    option = print_menu()
    if option == '1':
        old_pass = input('Please enter your password to encode: ')
        old_pass = encode(old_pass)
        print(old_pass)
    elif option == '2':
        new_pass = decode(old_pass)
        print(f'The encoded password is {old_pass}, and the original password is {new_pass}.')
