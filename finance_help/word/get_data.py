import pandas as pd
import random

def get_data():
    
    words = pd.read_csv("/Users/baeksujin/Desktop/finance_site/crawling.csv")
    word_name = words['name'].to_list()
    word_meaning = words['meaning'].to_list()

    word_index =[]
    num = random.randrange(0,len(words))

    for i in range(0,5):
        while num in word_index:
            num = random.randrange(0,len(words))
        word_index.append(num)

    random_word=[]

    for i in word_index:
        random_word.append(([word_name[i],word_meaning[i]]))
    return random_word

