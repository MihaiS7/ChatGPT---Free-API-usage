from cryptography.fernet import Fernet


def writing_file(file_name):
    file = open(file_name, 'wb')
    key = Fernet.generate_key()
    f = Fernet(key)
    username= input("Please enter the username: ").encode() # We need the input as bytes form for the encryption
    password = input("Please enter the password: ").encode()
    if len(username) > 0 and len(password) > 0:
        encrypt_username = f.encrypt(username)
        encrypt_password = f.encrypt(password)
        file.writelines([encrypt_username+b"\n", encrypt_password])
    file.close()
    # if you wanna see the decrypted code, just deactivate the below print statement
    # print(f.decrypt(encrypt_username), f.decrypt(encrypt_password))
    return str(username).decode(), str(password).decode()

def adding_to_ignore(name_file):
    f = open(".gitignore", 'r+')
    reading = f.read()
    if name_file not in reading:
        f.write(name_file)
    

file_name = "credentials.dev"
# writing_file(file_name)
adding_to_ignore(file_name)