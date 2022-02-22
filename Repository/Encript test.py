from cryptography.fernet import Fernet

def encrypt():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)

    with open("Clienti.txt", "rb") as f:
        data = f.read()
    print(data)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    print(encrypted)
    with open('Clienti.txt', "wb") as f:
        f.write(encrypted)


def decrypt():
    with open('key.key', 'rb') as f:
        key = f.read()

    with open("Clienti.txt", "rb+") as f:
        data = f.read()
        f.truncate(0)
        data2=f.read()

    print(data2)

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    decrypted = decrypted.decode()
    print(str(decrypted))

    with open('Clienti.txt', "w") as f:
        f.write(decrypted)




encrypt()
#decrypt()