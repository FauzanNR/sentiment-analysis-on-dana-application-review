import re
import unicodedata as unicdata
import string
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


sastra_stopword_factory = StopWordRemoverFactory()
indo_stop_words = set(stopwords.words('indonesian'))
eng_stop_words = set(stopwords.words('english'))
indo_stop_words.update(eng_stop_words)
indo_stop_words.update(['iya','yaa','gak','nya','na','sih','ku',"di","ga","ya","gaa","loh","kah","woi","woii","woy", "kok"])
indo_stop_words.update(set(sastra_stopword_factory.get_stop_words()))
factory = StemmerFactory()
the_stemmer = factory.create_stemmer()

def text_cleaner(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'#[A-Za-z0-9]+', '', text)
    text = re.sub(r'RT[\s]', '', text)
    text = re.sub(r"http\S+|https\S+", '', text)
    text = re.sub(r'[0-9]+', '', text)
    text = re.sub(r"wwww\S+", '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r"[²³¹]", "", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = unicdata.normalize('NFKD', text)
    text = text.replace('\n', ' ')
    text = text.strip(' ')
    return text


def stop_word_filter(text):
    words = text.split()
    for word in words:
        if word in indo_stop_words:
            words.remove(word)
    return ' '.join(words)

def text_stemmer(text): 
    stemmer=the_stemmer
    words = text
    stemmed_words = [stemmer.stem(word) for word in words] 
    return stemmed_words

def to_sentence(list_words): # Mengubah daftar kata menjadi kalimat
    sentence = ' '.join(word for word in list_words)
    return sentence
