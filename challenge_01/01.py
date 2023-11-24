def read_file(file: str) -> list:
    '''
    Lee el archivo con las palabras
    y las devuelve en una lista
    '''
    with open(file, 'r', encoding="utf-8") as text_file:
        file_contents = text_file.read()
        words_list = file_contents.split() 
    
    return words_list

data = read_file('data.txt')

def count_words(wordlist) -> dict:
    '''
    Crea un diccionario donde se va registrando
    cada palabra y las veces que aparece en la lista
    '''
    counter = {}
    for word in wordlist:
        if word not in counter:
            counter[word] = 1
        else:
            value = counter.get(word)
            counter[word] = value + 1
    return counter

count = count_words(data)

# Juntamos el resultado de contar todas las palabras en un string, en el formato especificado
string_counter = ''.join("{!s}{!r}".format(key,val) for (key,val) in count.items())
# e imprimimos dicho resultado
print('submit ' + string_counter)