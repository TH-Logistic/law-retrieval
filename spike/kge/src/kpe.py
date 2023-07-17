# Keyphrase extraction
from .stopwords import get_stop_words
import yake
import py_vncorenlp
import os
from .textrank.textrank import TextRank
# from wordwise import Extractor


class KeyPhraseExtraction:
    @staticmethod
    def yake(text: str, window_size: int = 3, max_candidates: int = 10):
        text = text.lower()
        stopwords = get_stop_words()

        # Khởi tạo YAKE với ngôn ngữ tiếng Việt sinh ứng viên 1-gram và 2-gram, với custom stopwrod
        kw_extractor = yake.KeywordExtractor(
            lan="vi", n=window_size, stopwords=stopwords
        )

        keywords = sorted(
            kw_extractor.extract_keywords(text), key=lambda x: x[1], reverse=True
        )[0:max_candidates]

        return keywords

    @staticmethod
    def textrank(text: str):
        t = TextRank(text)
        # Reference: https://github.com/lukhnos/textrank-study-python/blob/master/Key%20Phrase%20Extraction%20with%20Python.ipynb
        print(t.keywords(10))

    @staticmethod
    def textrank_v2(text: str):
        # extractor = Extractor(spacy_model="vi_core_news_lg")
        # keywords = extractor.generate(text)
        # print(keywords)
        pass

    @staticmethod
    def phobert(text: str):
        py_vncorenlp.download_model(os.getcwd() + '/py_vncorenlp_model')
        rdrsegmenter = py_vncorenlp.VnCoreNLP(
            annotators=["wseg"],
            save_dir='./py_vncorenlp_model'
        )
        ouput = rdrsegmenter.word_segment(text)
        print(ouput)
        pass
