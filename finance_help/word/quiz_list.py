import pymysql
import pandas as pd
from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


conn = pymysql.connect(host="localhost", 
                        user="root",
                        password=env('DB_PW'),
                        db = 'Finance_site',
                        charset='utf8')

print(env('DB_PW'))
curs = conn.cursor()

query = "select * from WORD_board where quiz={0}".format(1) # quiz가 1인값을 불러와서 퀴즈를 생성
curs.execute(query)

#data fetch
data = curs.fetchall()
print(data)
print(data[0][1])
conn.commit()
conn.close()


def make_quiz(word):
    meanings =[]
    for i in range(0,5):
        if word[i][0] in word[i][1].replace(" ",""):
            temp = word[i][1].replace(" ","")
            meaning = temp.replace(word[i][0],'[   정답   ]')
            print(meaning)
            meanings.append(meaning)
        else:
             meanings.append(word[i][1])

    return meanings

print(make_quiz(data))