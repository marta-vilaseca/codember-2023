def read_file(file: str) -> list[list]:
    '''
    Leemos el archivo y formateamos su contenido para poder iterar.
    Devuelve una lista de listas
    '''
    with open(file, 'r', encoding="utf-8") as text_file:
        contents = text_file.read() 
        temp_list = contents.replace('-',' ').split('\n')
        file_list = []
        for element in temp_list:
            file_list.append(element.split(' '))
    
    return file_list

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
    Iteramos por la lista de archivos, comprobamos si son 
    válidos (utilizando validate_checksum para comparar)
    y creamos una lista nueva con todos los checksum válidos
    '''
    valid_checksums = []
    for file in files:
        filename = file[0]
        checksum = file[1]
        valid_checksum = validate_checksum(filename)
        if checksum == valid_checksum:
            valid_checksums.append(checksum)
    return valid_checksums

# Imprimimos el checksum válido número 33
print(f"submit {valid_checksum_list(file_list)[32]}")