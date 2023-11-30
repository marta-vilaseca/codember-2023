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

file_list = read_file('files_quarantine.txt')

def validate_checksum(checksum: str) -> str: 
    '''
    Creamos lo que sería el checksum válido de cada elemento 
    de la lista, para poder compararlo después
    '''  
    valid_checksum = ''
    for character in checksum:
        if checksum.count(character) == 1:
            valid_checksum += character
    return valid_checksum

def valid_checksum_list(files: list[list]) -> list[str]:
    '''
    Iteramos por la lista de 
    '''
    has_valid_checksum = []
    for file in files:
        filename = file[0]
        checksum = file[1]
        valid_checksum = validate_checksum(filename)
        if checksum == valid_checksum:
            has_valid_checksum.append(checksum)
    return has_valid_checksum

# Imprimimos el checksum válido número 33
print(f"submit {valid_checksum_list(file_list)[32]}")