import random
import string


class PasswordGenerator:
   def generate_secure_password(self):
    min_len = input('Enter the length of the password: ')
    min_upper = input('Enter the number of capital letters: ')
    min_digit = input('Enter the number of digits: ')
    min_special = input('Enter the number of special characters: ')

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = '!@#$%^&*'

    password_list = []
    password_list += random.choices(uppercase, k=int(min_upper))
    password_list += random.choices(digits, k=int(min_digit))
    password_list += random.choices(special, k=int(min_special))

    remaining = int(min_len) - len(password_list)
    if remaining > 0:
        password_list += random.choices(lowercase, k=remaining)

    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    generator = PasswordGenerator()
    print('Welcome! Let\'s generate your own secure password.')
    print('Print \'X\' to go to the next step.')
    print('-' * 60)

    while True:
        password = input('Text here: ').strip()

        if password.lower() == 'x':
            pwd = generator.generate_secure_password()
            print(f'Your generated password is{pwd}')
            break


if __name__ == '__main__':
    main()
