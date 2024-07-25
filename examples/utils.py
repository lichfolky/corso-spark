import re


# da stringa ad array di tuple (parole,1)
def map_words(text):
    word_count = []
    words = tokenize(text)
    for word in words:
        word_count.append((word, 1))
    return word_count


# somma i valori degli elementi con la stessa chiave
def reduce_sum(key_value_list):
    new_cache = []
    current_key, current_value = ("", 1)
    for key, value in key_value_list:
        if current_key == key:
            current_value += value
        else:
            new_cache.append((current_key, current_value))
            current_key = key
            current_value = value

    new_cache.append((current_key, current_value))
    new_cache.remove(("", 1))
    return new_cache


# da stringa ad dizionario {parola,conteggio}
# le parole non sono ripetute!
def count_words(text):
    word_count = {}
    words = tokenize(text)
    for word in words:
        if word in word_count:
            word_count.update({word: word_count[word] + 1})
        else:
            word_count.update({word: 1})
    return word_count


def tokenize(text):
    trimmed_text = text.lower().strip()
    text_no_symbols = re.sub(r"[^\w]", " ", trimmed_text)
    return text_no_symbols.split()


print(map_words("Ciao a tutti, Ciao ciao, ciao"))
