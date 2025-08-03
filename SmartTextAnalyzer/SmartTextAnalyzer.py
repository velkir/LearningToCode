#Build SmartTextAnalyzer.py: read .txt, compute word frequency + unique word ratio,
#sentiment count (using simple positive/negative keywords).
#Provide sample input/output and docstrings.

import json
import collections


class TextAnalyzer:
    """An object that takes a text from user and provides methods to analyze it."""
    def __init__(self,
                 text_path,
                 sentiment_path,
                 stopword_filter=None):
        self.text = self._load_text(text_path)
        self.sentiment_dict = self._load_sentiment(sentiment_path)
        self.stopword_filter = self._load_stopword_filter(stopword_filter) if stopword_filter else None
        self.punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”«»‘’‚‛“”„‟‹›⹂'

    def analyze_text(self):
        """High-level function to fully analyze the text (frequency+unique words ratio + sentiment)"""
        word_frequency = self.compute_frequency()
        unique_words_ratio = self.compute_unique_words_ratio(word_frequency)
        sentiment = self.compute_sentiment_count(word_frequency)
        return {"word_frequency": word_frequency,
                "unique_word_ratio": unique_words_ratio,
                "sentiment": sentiment}

    def compute_frequency(self):
        """Computes each word's frequency in current text.
        Input sample:
        It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
        Output sample:
        {'a': 4, 'acknowledged': 1, 'be': 1, 'fortune': 1, 'good': 1, 'in': 2, 'is': 1, 'it': 1, 'man': 1, 'must': 1, 'of': 2, 'possession': 1, 'single': 1, 'that': 1, 'truth': 1, 'universally': 1, 'want': 1, 'wife': 1}
        """
        word_list = self._split_text(self.text)
        word_list = self._clean_words(word_list)
        if self.stopword_filter:
            word_list = self._stopword_filter(word_list)
        word_frequency = self._transform_list_to_dict(word_list)
        return word_frequency

    def compute_unique_words_ratio(self, word_frequency=None):
        """Computes each word's ratio against all-words' count.
        Input sample:
        It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
        Output sample:
        {'a': 0.174, 'acknowledged': 0.043, 'be': 0.043, 'fortune': 0.043, 'good': 0.043, 'in': 0.087, 'is': 0.043, 'it': 0.043, 'man': 0.043, 'must': 0.043, 'of': 0.087, 'possession': 0.043, 'single': 0.043, 'that': 0.043, 'truth': 0.043, 'universally': 0.043, 'want': 0.043, 'wife': 0.043}
        """
        if not word_frequency:
            if self.text:
                word_frequency = self.compute_frequency()
            else:
                raise FileNotFoundError("Please provide a text file to analyze unique words ratio.")
        all_words_count = 0
        for v in word_frequency.values():
            all_words_count += v
        words_ratio = {word:round(count/all_words_count, 3) for word, count in word_frequency.items()}
        return words_ratio

    def compute_sentiment_count(self, word_frequency=None):
        """Computes positive/negative sentiment words count according to the provided sentiment dictionary (sentiment.json by default)
        Input sample:
        It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
        Output sample:
        {'negative': 0, 'positive': 1}
        """
        if not word_frequency:
            if self.text:
                word_frequency = self.compute_frequency()
            else:
                raise FileNotFoundError("Please provide a text to analyze unique words ratio.")
        positive = sum(v for k, v in word_frequency.items() if self.sentiment_dict.get(k) == "positive")
        negative = sum(v for k, v in word_frequency.items() if self.sentiment_dict.get(k) == "negative")
        return {"positive":positive, "negative":negative}

    def _load_text(self, text_path):
        """Loads a text from a text file from provided path to self.text"""
        try:
            with open(text_path) as f:
                text = f.read()
                return text
        except:
            raise FileNotFoundError("Please provide a correct path to a text file.")

    def _load_sentiment(self, sentiment_dict):
        """Loads a sentiment dictionary from a json file from provided path to self.sentiment_dict"""
        try:
            with open(sentiment_dict, "r", encoding="utf-8") as f:
                sentiment_dict_en = json.load(f)
                return sentiment_dict_en
        except:
            raise FileNotFoundError("Please provide a correct path to a sentiment json-file.")

    def _load_stopword_filter(self, stopword_filter_path):
        """Loads a list of words from txt-file that won't be analyzed as they don't have a meaning by their own"""
        try:
            with open(stopword_filter_path) as f:
                stopword_filter = f.read()
                stopword_filter_list = stopword_filter.split("\n")
                return stopword_filter_list
        except:
            raise FileNotFoundError("Please provide a correct path to a sentiment json-file.")

    def _split_text(self, text):
        """Splits the text into list of words"""
        text = text.replace("\n", " ")
        words_list = text.split(" ")
        return words_list

    def _clean_words(self, word_list):
        """Cleans words from punctuational characters"""
        return [word.strip(self.punctuation_chars).lower() for word in word_list if word]

    def _transform_list_to_dict(self, word_list):
        """Transforms list of words into a dictionary of format word:number_of_times_used_in_text"""
        return dict(collections.Counter(word_list))

    def _stopword_filter(self, word_list):
        """Filters meaningless words according to stopword_filter text file."""
        return [word for word in word_list if word not in self.stopword_filter]

analyzer = TextAnalyzer(text_path="text.txt",
                        sentiment_path="sentiment.json",
                        stopword_filter="stopword_filter.txt"
                        )
results = analyzer.analyze_text()