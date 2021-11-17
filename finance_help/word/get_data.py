import pandas as pd
import random

def get_data():
    
    words = pd.read_csv("C:\\project\\finance\\data\\단어사전크롤링.csv")
    word_name = words['name'].to_list()
    word_meaning = words['meaning'].to_list()

    word_index =[]
    num = random.randrange(0,len(words))

    for i in range(0,5):
        while num in word_index:
            num = random.randrange(0,len(words))
        word_index.append(num)

    #print(word_index)

    random_word=[]

    for i in word_index:
        #print(word_name[i],"에 대한 설명입니다")
        #print("의미 : ",word_meaning[i])
        random_word.append(([word_name[i],word_meaning[i]]))
    return random_word

#print(get_data())