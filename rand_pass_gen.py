import random
import string

def generate_password(length):
   
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password
password = generate_password(int(input("Enter The Value: ")))
print(password)
