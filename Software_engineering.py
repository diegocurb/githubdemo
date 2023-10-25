# Diego Curbelo
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    option = input('Please enter an option: ')
    return option

def decode(secret):
    password = ""
    for i in secret:
        each_dig_password = (int(i) - 3) % 10
        password += str(each_dig_password)
    print(password)

