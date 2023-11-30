import re

def read_file(file: str) -> list[list]:
    '''
    Leemos el archivo y formateamos su contenido para poder iterar.
    Devuelve una lista de listas
    '''
    with open(file, 'r', encoding="utf-8") as text_file:
        contents = text_file.read() 
        temp_list = contents.replace('-',' ').replace(':','').split('\n')        
        user_list = []
        for element in temp_list:
            user_list.append(element.split(','))
    
    return user_list

database = read_file('database_attacked.txt')

def validate_user(user: list) -> bool:
    '''
    Recibe cada línea de usuario en forma de lista
    y comprueba si TODOS los datos son válidos
    '''
    is_valid = False
    valid_userid = False
    valid_username = False
    valid_email = False
    valid_age = False
    valid_location = False

    # Comprueba si un valor es string vacío o None
    def is_not_empty(item):
        if item != '' or item != None:
            return True
        else:
            return False
    
    # Validamos id
    userid = user[0]
    if userid.isalnum() and is_not_empty(userid):
        valid_userid = True
    
    # Validamos username
    username = user[1]
    if username.isalnum() and is_not_empty(username):
        valid_username = True

    # Validamos email
    email = user[2]
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if (re.fullmatch(regex, email)):
        valid_email = True

    # Validamos age
    age = user[3]
    if age == '' or age.isdigit() == True:
        valid_age = True

    # Validamos location
    location = user[4]
    if type(location) == str or location == '':
        valid_location = True

    # Si todo es válido, el usuario es válido
    if valid_userid and valid_username and valid_email and valid_age and valid_location:
        is_valid = True
    
    return is_valid

def get_invalid_users(db: list[list]) -> list[list]:
    '''
    Recorre toda la BD de usuarios y guarda
    todos los usuarios no válidos en una lista
    '''
    invalid_users = []

    for user in db:
        if validate_user(user) == False:
            invalid_users.append(user)
    
    return invalid_users

def secret_message(invalid_users: list) -> str:
    '''
    Itera por la lista de usuarios inválidos que 
    hemos generado y forma el mensaje secreto con
    la primera letra de cada username
    '''
    message = ''
    for user in invalid_users:
        first_letter = user[1][0]
        message += first_letter
    
    return message

# Imprimimos el mensaje secreto
print(f"submit {secret_message(get_invalid_users(database))}")
