import random
def generate_password(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    characters = letters + digits + punctuation 
    password = ''
    for _ in range(length):
        password += characters[int(len(characters) * random.random())]
    return password
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated password:", password) 