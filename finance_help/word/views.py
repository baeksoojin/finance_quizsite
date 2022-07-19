from multiprocessing.connection import answer_challenge
from unicodedata import name
from django.shortcuts import render, redirect
import random
import sys
sys.path.append('C:\\project\\finance\\finance_help\\word')
from word.models import WORD,Wrong
from .crawling import crawling
from django.db.models import Max
from .quiz_list import quiz_list


def list(request):
    word_board = WORD
    res_data={}
    data=[]
    if request.method == "POST":

        # max_id=word_board.objects.all().aggregate(max_id=Max("id"))['max_id']
        # for i in range(0,5):
        #     pk = random.randint(1,max_id)
        #     data.append(word_board.objects.get(pk=pk))
        # res_data['all_word_board'] = data
        
        # 이전 5개의 선택된 데이터들의 quiz항목을 False로 변경후 저장
        if(word_board.objects.filter(quiz = True)):
            before_data = word_board.objects.filter(quiz = True)
            for i in before_data:
                print(i)
                i.quiz = False
                i.save()
        # 새로운 5개의 데이터를 선택하고 quiz 항목을 True로 저장
        all_word_board = word_board.objects.all()
        random_data = all_word_board.order_by('?')[:5]
        for i in random_data:
            print(i)
            i.quiz = True
            i.save()
        print("======================>",random_data)

        res_data['random_data'] = random_data
        return render(request,'word/word_list.html',res_data)
    else:
        # 단어가 db에 없는 경우를 대비.
        if not word_board.objects.all():
            datas = crawling()
            
            print(len(datas['name']))
            for i in range(0,len(datas['name'])):
                print(datas['name'][i])
                print(datas['meaning'][i])
                word_board(name = datas['name'][i], meaning = datas['meaning'][i]).save()
        # 단어가 db에 존재할때
        else:
            #맨 처음이라 quiz가 모두 False인 경우를 대비
            if(word_board.objects.filter(quiz = True)):
                before_data = word_board.objects.filter(quiz = True)
                for i in before_data:
                    print(i)
                    i.quiz = False
                    i.save()
            # 보여줄 5개만 True로 quiz속성을 저장
            all_word_board = word_board.objects.all()
            random_data = all_word_board.order_by('?')[:5]
            for i in random_data:
                print("random_data : ",i)
                i.quiz = True
                i.save()
            print("======================>",random_data)
            res_data['random_data'] = random_data
            return render(request, 'word/word_list.html',res_data)


from django.core import serializers


def quiz(request):

    if request.method == "POST":

        
        word = WORD
        all_word_board = word.objects.all()
        quiz_data = all_word_board.filter(quiz = True)

        mix_quiz = quiz_data.order_by('?')[:5]
        
        temp = quiz_list()
        print("===============>>>>",temp) 
        # 퀴즈속에 문제답이 있는 경우가 있고 이를 처리하기 위해 만들어놓은 함수를 적용시킨다.

        res_data={
        "quiz_data": mix_quiz,
        "quiz_js": serializers.serialize('json',mix_quiz),
        }

        return render(request, 'word/quiz.html',res_data)


        
    else:
        return redirect('/word/list')

def result(request):

    if request.method == "POST":

        answers = request.POST["answers"]
        checks = request.POST["checks"]
        answers=answers.split(",")
        checks=checks.split(",")
        print(answers)
        print(checks)

        wrong = Wrong()
        word = WORD

        all_word_board = word.objects.all()

        corrects=[]
        wrongs=[]

        for i in range(0,5):
            if answers[i]==checks[i]:
                corrects.append(int(answers[i]))
            else:
                wrongs.append(int(answers[i]))

        print(corrects, wrongs)

        wrong_words=[]
        for i in wrongs:
            wrong_word = all_word_board.get(id=i)
            wrong.quiz = wrong_word
            wrong.save()
            wrong_words.append(all_word_board.get(id=i).name)

        # #모든 wrong_word board를 10개씩 한페이지에서 출력
        print("!!!=>",wrong_words)
        res_data = {}
        if len(wrongs):
            res_data['score'] = str(len(corrects))+"개 정답입니다!"
            res_data['wrongs'] = wrong_words
        else:
            res_data['score'] = "모두 정답입니다><"

        return render(request,'word/result.html',res_data)


# def list 만들어서 위에서 틀린 것들만 저장. redirect해서 list에서 model에 저장하고 한 페이지에 최근 10개 보여주기.
