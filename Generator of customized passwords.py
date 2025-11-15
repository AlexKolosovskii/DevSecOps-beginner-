import random
import string
import argparse


def generate_secure_password(min_len, min_upper, min_digit, min_special):
    if min_len < (min_upper + min_digit + min_special):
        raise ValueError('Password length is too short for the given requirements')

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = '!@#$%^&*'

    password_list = []
    password_list += random.choices(uppercase, k=min_upper)
    password_list += random.choices(digits, k=min_digit)
    password_list += random.choices(special, k=min_special)

    remaining = min_len - len(password_list)
    if remaining > 0:
        password_list += random.choices(lowercase, k=remaining)

    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    parser = argparse.ArgumentParser(description='Generate your password based on the given criteria')
    parser.add_argument('--length', type=int, required=True, help='Length of the password')
    parser.add_argument('--upper', type=int, required=True, help='Minimum number of uppercase letters')
    parser.add_argument('--digits', type=int, required=True, help='Minimum number of digits')
    parser.add_argument('--special', type=int, required=True, help='Minimum number of special characters')

    args = parser.parse_args()

    try:
        password = generate_secure_password(args.length, args.upper, args.digits, args.special)
        print(f'Your generated password is {password}')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
