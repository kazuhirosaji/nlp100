

def get_ngram(n, s):
    words = []
    s = s.replace(' ', '')
    for key, val in enumerate(s):
        words.append(s[key:key+n])
    return words

def get_ngram_word(n, s):
    words = s.split(' ')
    for key, val in enumerate(words):
        words.append((' '.join(words[key:key+n])))
    return words
