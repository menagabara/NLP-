import re
import nltk
nltk.download('punkt')
from nltk import *
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')


def split_into_sentences(txt):
    # split by punctuation.
    txt_list = re.split(r'\,|\.|\:|\;|\"|\{|\}|\[|\]|\\|\/|\+|\-|\(|\)|\*|\&|\^|\%|\$|\#|\@|\!|\~|>|\<|\?', txt.casefold())

    # remove leading and trailing spaces from the list.
    txt_list = [x.strip() for x in txt_list]

    # remove empty items.
    txt_list = list(filter(None, txt_list))

    return txt_list


def split_into_words(sentence):
    # split by space.
    words = sentence.split()
    for word in words:
        print(word)


# split using nltk.
def nltk_func():
    sentencesList = nltk.sent_tokenize(txt)
    for sentence in sentencesList:
        word = nltk.word_tokenize(sentence)
        print(word)


txt = "hello, my name is Mena. i'm a 25 years old. from Alexanderia. i work as a software engineer. what about you?"
sentences = split_into_sentences(txt)

for sentence in sentences:
    split_into_words(sentence)

nltk_func()




