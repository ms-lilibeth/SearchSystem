from SearchSystem import *
from os import listdir
from os.path import isfile, join


dir_name = "text_collection/"
if __name__=="__main__":
    files = [join(dir_name, f) for f in listdir(dir_name) if isfile(join(dir_name, f))]

    # filename = "sometext.txt"

    # with open(filename, 'r') as f:
    #     text = f.read()
    #
    # print(text)
    # print("========================")
    # text = lexical_analysis(text)
    # print(text)
    # print("========================")
    # text = delete_stop_words(text)
    # print(text)
    # print("========================")
    # text = stemming(text)
    # print(text)
    # print("========================")
