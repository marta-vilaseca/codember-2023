f = open('data.txt', 'r')
file_contents = f.read()

data = file_contents.split()
# print(wordlist)

def count_words(wordlist):
    counter = {}
    for word in wordlist:
        if word not in counter:
            counter[word] = 1
        else:
            value = counter.get(word)
            counter[word] = value + 1
    return counter

count = count_words(data)

string_counter = ''.join("{!s}{!r}".format(key,val) for (key,val) in count.items())
print('submit ' + string_counter)

f.close()