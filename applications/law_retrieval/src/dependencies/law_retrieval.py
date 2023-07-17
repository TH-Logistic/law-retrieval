import re
import string
from pyvi.ViTokenizer import tokenize # Vietnamese tokenizer
import os.path
stopwords_file = open(os.path.dirname(__file__) + '/../stopwords')
class LawRetrieval:
    def __init__(self,query:str) -> None:
        self.query=query
        pass
    
    def cleanse(self) -> None:
        self.query = re.sub('<.*?>','',self.query).strip()
        self.query = re.sub('(\s)+', r'\1', self.query)
        
    def sentence_segment(self):
        sents = re.split("([.?!])?[\n]+|[.?!] ", self.query)
        return sents
    
    def word_segment(self):
        self.query = tokenize(self.query)
    
    def normalize_text(self):
        listpunctuation = string.punctuation.replace('_', '')
        for i in listpunctuation:
            self.query = self.query.replace(i, ' ')
        return self.query.lower()
    
    def remove_special_characters(self):
        chars = re.escape(string.punctuation)
        return re.sub(r'['+chars+']', '', self.query)
    
    def remove_stopword(self):
        list_stopwords = stopwords_file.readlines()

        pre_text = []
        words = self.query.split()
        for word in words:
            if word not in list_stopwords:
                pre_text.append(word)
            text2 = ' '.join(pre_text)
        self.query = text2

    def standardize(self):
        self.cleanse()
        self.remove_special_characters()
        self.word_segment()
        self.normalize_text()
        self.remove_stopword()
        pass
