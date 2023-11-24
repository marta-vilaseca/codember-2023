def read_file(file: str) -> str:
    '''
    Leemos el archivo y formateamos su contenido para poder iterar.
    Devuelve una lista de tuplas
    '''
    with open(file, 'r', encoding="utf-8") as text_file:
        contents = text_file.read() 
        temp_list = contents.replace('-',' ').replace(':','').split('\n')        
        password_list = []
        for element in temp_list:
            password_list.append(element.split(' '))
    
    return password_list

pw_list = read_file('encryption_policies.txt')

def check_policies(password_list:list[list]) -> list[list]:
    '''
    Recibe la lista de tuplas con los passwords y los
    va comprobando. Si no cumplen las condiciones,
    los guarda en la lista de invalid_passwords.
    Devuelve la lista de invalid_passwords
    '''
    invalid_passwords = []

    for line in password_list:
        min = int(line[0])
        max = int(line[1])
        character = line[2]
        password = line[3]

        num_of_occurences = password.count(character)
        if num_of_occurences < min or num_of_occurences > max:
            invalid_passwords.append(password)
    
    return invalid_passwords

invalid_pw = check_policies(pw_list)

# Recogemos e imprimimos el password número 42 en la lista
print(f"submit {invalid_pw[41]}")