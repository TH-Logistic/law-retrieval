# Keyphrase extraction
from .stopwords import get_stop_words
import yake
import spacy
import pytextrank


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
    def textrank(nlp: spacy.language.Language, text: str):
        if not nlp.has_pipe("textrank"):
            nlp.add_pipe("textrank")
        text = text.lower()
        doc = nlp(text)
        for phrase in doc._.phrases:
            print(phrase.text)
            print(phrase.rank, phrase.count)
            print(phrase.chunks)
        return text
