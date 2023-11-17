# SIGNIFICADO:
"""
"#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual.
"""
f = open('data.txt', 'r')
file_contents = f.read()

def compiler(message):
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

print('submit ' + compiler(file_contents))

f.close()