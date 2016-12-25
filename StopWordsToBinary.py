import pickle
import re

if __name__=="__main__":
    words = []
    with open("stop-words-rus.txt", 'r', encoding='utf-8') as f:
        for line in f:
            word = line.replace('\n','')
            words.append(word)
    words[0] = "как"
    print(words)
    with open("stop-words-binary","wb") as f:
        pickle.dump(words, f)