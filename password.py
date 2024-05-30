import random

def password_generator(length):
    characters = "abcdefghijklmnopqrstuvwxyz@#$%&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print(password_generator(length))
