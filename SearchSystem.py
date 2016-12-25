import Stemmer
import re
import pickle
from collections import Counter, defaultdict
import math

class Searcher:
    @staticmethod
    def lexical_analysis(text):
        return [r.group().lower() for r in re.finditer(r'\w+', text)]

    @staticmethod
    def stemming(text):
        stemmer = Stemmer.Stemmer('russian')
        return stemmer.stemWords(text)
        pass

    @staticmethod
    def delete_stop_words(text):
        stop_words = pickle.load(open("stop-words-binary",'rb'))
        return [w for w in text if w not in stop_words]

    def __init__(self, files):
        self.data = {}
        for file in files:
            with open(file, encoding='utf-8') as f:
                text = self.lexical_analysis(f.read())
                text = self.stemming(self.delete_stop_words(text))
                self.data[file] = Counter(text)

    def tf(self, term, file):
        return self.data[file][term] / sum(self.data[file].values())

    def idf(self, term):
        count = 0
        for stat in self.data.values():
            if term in stat:
                count += 1
        return 0 if count == 0 else math.log(len(self.data) / count)

    def tf_idf(self, term, file):
        return self.tf(term, file) * self.idf(term)

    def search(self, query):
        terms = set(self.stemming(self.delete_stop_words(self.lexical_analysis(query))))
        stats = defaultdict(lambda: 0)
        for term in terms:
            for file in self.data:
                stats[file] += self.tf_idf(term, file)
        return stats


if __name__=="__main__":
    pass
    # print(lexical_analysis("Мама: мыла раму!"))