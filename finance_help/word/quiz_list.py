import pymysql
import pandas as pd
from pathlib import Path
import environ
import os
import json

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

def quiz_list():

    conn = pymysql.connect(host="localhost", 
                            user="root",
                            password=env('DB_PW'),
                            db = 'Finance_site',
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)

    print(env('DB_PW'))
    curs = conn.cursor()
    query = "select * from WORD_board where quiz={0}".format(1) # quiz가 1인값을 불러와서 퀴즈를 생성
    curs.execute(query)
    data = curs.fetchall()
    print(data)
    print(data[0]['meaning'])
    conn.commit()

    def make_quiz(word):
        meanings =[]

        for i in range(0,5):
            if word[i]["name"] in word[i]["meaning"].replace(" ",""):
                temp = word[i]["meaning"].replace(" ","")
                meaning = temp.replace(word[i]["name"],'[   정답   ]')
                print("!!!!!!!!!!!!!!!",meaning)
                meanings.append(meaning)
                data[i]["meaning"] = meaning
                query = """update WORD_board set quiz_meaning = %s where id = %s"""
                
                print("=================>",query)
                t = (meaning,word[i]["id"])
                print(t)

                curs.execute(query,t)
                
                conn.commit()
            else:
                meanings.append(word[i]["meaning"])    
        return pd.DataFrame(data)


    print(make_quiz(data))
    conn.close()

    # database에 quiz를 저장하는 과정을 진행하면 됨.


quiz_list()