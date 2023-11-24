# SIGNIFICADO:
"""
"#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual.
"""

def read_file(file: str) -> str:
    '''
    Lee el archivo y devuelve
    el mensaje cifrado en formato string
    '''
    with open(file, 'r', encoding="utf-8") as text_file:
        file_contents = text_file.read() 
    
    return file_contents

secret_message = read_file('data.txt')

def compiler(message) -> int:
    '''
    Calcula el significado del mensaje cifrado
    de acuerdo a las especificaciones dadas.
    Devuelve un entero.
    '''
    translated = ''
    current_value = 0
    for character in message:
        if character == '#':
            decoded_character = current_value + 1
        elif character == '@':
            decoded_character = current_value - 1
        elif character == '*':
            decoded_character = current_value**2
        elif character == '&':
            decoded_character = current_value
            translated += str(decoded_character)

        current_value = int(decoded_character)
        
    return translated

# Imprimimos el resultado de decodificar el mensaje
print('submit ' + compiler(secret_message))