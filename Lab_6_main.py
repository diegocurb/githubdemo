# Davey
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
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
    return new_password


option = '0'
while option != '3':
    option = print_menu()
    if option == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
    elif option == '2':
        decoded_password = decode(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
