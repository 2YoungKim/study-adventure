import random

def genPass() :
    reference = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="
    password = ""

    for i in range(6):
        index = random.randrange(len(reference))
        password = password + reference[index]
    return password

print(genPass())