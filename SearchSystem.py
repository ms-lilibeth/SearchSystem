import Stemmer
import sklearn
import re
import pickle


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

    def get_tf_idf_features(text):
        pass


if __name__=="__main__":
    # print(lexical_analysis("Мама: мыла раму!"))