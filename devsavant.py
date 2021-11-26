# 2 functions 
#  def first(string): va a tomar una frase del string y va a tomar las palabras que contiene y la frecuencia que se usa esa frase
# 'Daniel hola' Daniel:1

# toma lo que retorna la segunda y devuelva una tupla con la palabra mas repetida y su respectiva frecuencia

def func_1(phrase):
    words = {}
    for word in phrase.split(' '):
        if(words.get(word.lower(), False)):
            words[word.lower()] += 1
        else:
            words[word.lower()] = 1
    return words

def func_2(words):
    tupla = ('word', 0)
    for word, value in words.items():
        if(tupla[1] < value):
            tupla = (word, value)
    return tupla

func_1_ret = func_1('Marcos Ivan Rey Is the best marcos best MaRcos')
print(func_1_ret)
print(func_2(func_1_ret))

