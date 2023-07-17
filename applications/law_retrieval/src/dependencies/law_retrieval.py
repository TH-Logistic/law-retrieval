import re
import string
from pyvi.ViTokenizer import tokenize  # Vietnamese tokenizer
import os.path
stopwords_file = open(os.path.dirname(__file__) + '/../stopwords.txt')
stopwords = list(
    map(lambda s: s.strip(), stopwords_file.readlines())
)


class LawRetrieval:
    def __init__(self, query: str) -> None:
        self.query = query
        self.standardize()
        pass

    def cleanse(self) -> None:
        self.query = re.sub('<.*?>', '', self.query).strip()
        self.query = re.sub('(\s)+', r'\1', self.query)

    def sentence_segment(self):
        self.query = re.split("([.?!])?[\n]+|[.?!] ", self.query)
        return self.query

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
        pre_text = []
        words = self.query.split()
        for word in words:
            if word not in stopwords:
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

    def keyphrases(self) -> list[str]:
        return self.query.split()
