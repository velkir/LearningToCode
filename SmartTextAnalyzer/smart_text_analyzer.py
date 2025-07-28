import json
import collections


class TextAnalyzer:
    """An object that takes a text from user and provides methods to analyze it."""
    def __init__(self):
        self.text = None
        self.sentiment_dict = None
        self.punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~“”'

    def analyze_text(self):
        words_frequency = self.compute_frequency()
        unique_words_ratio = self.compute_unique_words_ratio(words_frequency)
        sentiment = self.compute_sentiment_count(words_frequency)
        return {"Words_frequency": words_frequency,
                "Unique words ratio": unique_words_ratio,
                "Sentiment": sentiment}

    def compute_frequency(self):
        """Computes each word's frequency in current text.
        Input sample:
        It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
        Output sample:
        {'a': 4, 'acknowledged': 1, 'be': 1, 'fortune': 1, 'good': 1, 'in': 2, 'is': 1, 'it': 1, 'man': 1, 'must': 1, 'of': 2, 'possession': 1, 'single': 1, 'that': 1, 'truth': 1, 'universally': 1, 'want': 1, 'wife': 1}
        """
        words_list = self._split_text(self.text)
        words_list = self._clean_words(words_list)
        words_frequency = self._transform_list_to_dict(words_list)
        return words_frequency

    def compute_unique_words_ratio(self, words_frequency=None):
        """Computes each word's ratio against all-words' count.
        Input sample:
        It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
        Output sample:
        {'a': 0.174, 'acknowledged': 0.043, 'be': 0.043, 'fortune': 0.043, 'good': 0.043, 'in': 0.087, 'is': 0.043, 'it': 0.043, 'man': 0.043, 'must': 0.043, 'of': 0.087, 'possession': 0.043, 'single': 0.043, 'that': 0.043, 'truth': 0.043, 'universally': 0.043, 'want': 0.043, 'wife': 0.043}
        """
        if not words_frequency:
            if self.text:
                words_frequency = self.compute_frequency()
            else:
                raise ValueError("Please provide a text to analyze unique words ratio.")
        all_words_count = 0
        for v in words_frequency.values():
            all_words_count += v
        words_ratio = {word:round(count/all_words_count, 3) for word, count in words_frequency.items()}
        return words_ratio

    def compute_sentiment_count(self, words_frequency=None):
        """Computes positive/negative sentiment words count according to the provided sentiment dictionary (sentiment.json by default)
        Input sample:
        It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
        Output sample:
        {'negative': 0, 'positive': 1}
        """
        if not words_frequency:
            if self.text:
                words_frequency = self.compute_frequency()
            else:
                raise ValueError("Please provide a text to analyze unique words ratio.")
        positive = 0
        negative = 0
        for word, count in words_frequency.items():
            if word in self.sentiment_dict.keys():
                freq = words_frequency[word]
                if self.sentiment_dict[word]=="positive":
                    positive+=1*freq
                elif self.sentiment_dict[word]=="negative":
                    negative+=1*freq
        return {"positive":positive, "negative":negative}

    def load_text(self, path="text.txt"):
        """Loads a text from a text file from provided path to self.text"""
        try:
            with open(path) as f:
                text = f.read()
                self.text = text
        except:
            raise ValueError("Please provide a correct path to a text file.")

    def load_sentiment(self, sentiment_dict="sentiment.json"):
        """Loads a sentiment dictionary from a json file from provided path to self.sentiment_dict"""
        try:
            with open(sentiment_dict, "r", encoding="utf-8") as f:
                sentiment_dict_en = json.load(f)
                self.sentiment_dict = sentiment_dict_en
        except:
            raise ValueError("Please provide a correct path to a sentiment json-file.")

    def _split_text(self, text):
        """Splits the text into list of words"""
        text = text.replace("\n", " ")
        words_list = text.split(" ")
        return words_list

    def _clean_words(self, words_list):
        """Cleans words from punctuational characters"""
        return [word.strip(self.punctuation_chars).lower() for word in words_list if word]

    def _transform_list_to_dict(self, words_list):
        """Transforms list of words into a dictionary of format word:number_of_times_used_in_text"""
        return dict(collections.Counter(words_list))


analyzer = TextAnalyzer()
analyzer.load_text("text3.txt")
analyzer.load_sentiment()
results = analyzer.analyze_text()
pass
