import openpyxl as op
import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download()

wb = op.load_workbook("rocket_stop_word_removed.xlsx")

ws = wb['Sheet1']

lemmatizer = WordNetLemmatizer()

def just_lemmatize(sentence):
    words = word_tokenize(sentence)

    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    lemmatized_sentence = ' '.join(lemmatized_words)

    return lemmatized_sentence


for cell in ws['A']:
    if isinstance(cell.value, str):
        cell.value = just_lemmatize(cell.value)

wb.save('lemmatized_rocket.xlsx')
