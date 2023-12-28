# from cryptography.fernet import Fernet


def writing_file(file_name):
    file = open(file_name, 'w')
    username= input("Please enter the username: ")
    password = input("Please enter the password: ")
    if len(username) > 0 and len(password) > 0:
        file.writelines([username+"\n", password])
    file.close()
    return username, password

def adding_to_ignore(name_file):
    f = open(".gitignore", 'r+')
    reading = f.read()
    if name_file not in reading:
        f.write(name_file)
    
    
file_name = "credentials.dev"
# writing_file(file_name)
adding_to_ignore(file_name)