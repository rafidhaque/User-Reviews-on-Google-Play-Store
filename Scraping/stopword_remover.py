import re
import string
import nltk

nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')

def clean_sentence(sentence):
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    sentence = sentence.lower().split()

    sentence = [word for word in sentence if word not in stop_words]

    sentence = ' '.join(sentence)

    return sentence

