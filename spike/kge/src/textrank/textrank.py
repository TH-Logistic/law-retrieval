import networkx as nx

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import os
import re
from ..stopwords import get_stop_words

QUOTES = re.compile(r'[’‘“”]')


class TextRank:
    def __init__(self, text: str):

        tfidf_vectorizer = TfidfVectorizer(stop_words=get_stop_words())
        sentence_tokenizer = PunktSentenceTokenizer()

        self.sentences = sentence_tokenizer.tokenize(text)
        bow_matrix = tfidf_vectorizer.fit_transform(self.sentences)
        self.tfidf_features = tfidf_vectorizer.get_feature_names_out()

        sentence_similarity_matrix = bow_matrix * bow_matrix.T
        word_similarity_matrix = bow_matrix.T * bow_matrix

        self.sentence_nx_graph = nx.convert_matrix.from_scipy_sparse_array(
            sentence_similarity_matrix)
        self.word_nx_graph = nx.convert_matrix.from_scipy_sparse_array(
            word_similarity_matrix)
        self.__sentence_pagerank = None
        self.__word_pagerank = None

    def get_sentence(self, index):
        return self.sentences[index]

    def get_word(self, index):
        return self.tfidf_features[index]

    def plot_sentence_graph(self):
        self.plot_graph(self.sentence_nx_graph)

    def plot_word_graph(self):
        self.plot_graph(self.word_nx_graph)

    def plot_graph(self, graph):
        nx.draw(graph, with_labels=True)
        plt.show()
        plt.close()

    def key_sentences(self, topn=None):
        if not self.__sentence_pagerank:
            self.__sentence_pagerank = nx.pagerank(self.sentence_nx_graph)
        return sorted(((self.__sentence_pagerank[i], s) for i, s in enumerate(self.sentences)),
                      reverse=True)[:topn]

    def keywords(self, topn=None):
        if not self.__word_pagerank:
            self.__word_pagerank = nx.pagerank(self.word_nx_graph)
        return sorted(((self.__word_pagerank[i], s) for i, s in enumerate(self.tfidf_features)),
                      reverse=True)[:topn]
