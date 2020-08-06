import hashlib
import os

users = {}  

username = 'Brent'
password = 'mypassword'

salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {
    'salt': salt,
    'key': key
}

username = 'Brent'
password = 'notmypassword'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key != new_key


username = 'Brent'
password = 'mypassword'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key

username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {
    'salt': salt,
    'key': key
}

username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key