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

words = pd.read_csv('/Users/baeksujin/Desktop/Helfin/finance_quizsite/finance_help/word/finance_words.csv')
print(words.head())
words = words.dropna()
print("_______________")
words = words.reset_index(drop=True)
print(words.head())
sql_rows = []
for i in range(0,len(words)):
    sql_row = (words['word'][i],words['meaning'][i],0)
    sql_rows.append(sql_row)

print(sql_rows)

insert_words = """insert into WORD_board(name,meaning,quiz) values (%s, %s, %s)"""
# curs.executemany(insert_words,sql_rows)
conn.commit()
conn.close()