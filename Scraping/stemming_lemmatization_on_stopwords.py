import openpyxl as op
import nltk
import re

nltk.download('wordnet')

wb = op.load_workbook("rocket_stop_word_removed.xlsx")

ws = wb['Sheet1']

def stem_lemmatize(sentence):
    tokenizer = nltk.tokenize.WhitespaceTokenizer()
    stemmer = nltk.stem.PorterStemmer()
    lemmatizer = nltk.stem.WordNetLemmatizer()

    words = tokenizer.tokenize(sentence)

    stemmed_words = [stemmer.stem(word) for word in words]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]

    stemmed_lemmatized_sentence = ' '.join(lemmatized_words)

    return stemmed_lemmatized_sentence

for cell in ws['A']:
    if isinstance(cell.value, str):
        cell.value = stem_lemmatize(cell.value)

wb.save('stem_lemmatized_rocket.xlsx')
