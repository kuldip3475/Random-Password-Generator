import random
import string


pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

print(random.choice(charValues))

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is : ", password)


