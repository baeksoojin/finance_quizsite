from django.shortcuts import render, redirect
import random
import sys
sys.path.append('C:\\project\\finance\\finance_help\\word')
from word.models import WORD,QUIZ
from .crawling import crawling
from django.db.models import Max


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
        
        # django random 정렬 -> ?를 사용할 수 있는데 이것은 아래의 두줄로 위의 5줄을 커버가능.

        all_word_board = word_board.objects.all()
        res_data['all_word_board'] = all_word_board.order_by('?')[:5]
        return render(request,'word/word_list.html',res_data)
    else:
        
        if not word_board.objects.all():
            datas = crawling()
            
            print(len(datas['name']))
            for i in range(0,len(datas['name'])):
                print(datas['name'][i])
                print(datas['meaning'][i])
                word_board(name = datas['name'][i], meaning = datas['meaning'][i]).save()
        
        if word_board.objects.all():
            all_word_board = word_board.objects.all()
            res_data['all_word_board'] = all_word_board.order_by('-id')[:5]
        return render(request, 'word/word_list.html',res_data)


from django.core import serializers


def quiz(request):

    if request.method == "POST":

       
        word = WORD
        print(type(word))
        all_word_board = word.objects.all()
        word_board = all_word_board.order_by('-id')[:5]

        list=[]
        word_index=[]
        num = random.randrange(0,5)
        for i in range(0,5):
            while num in word_index:
                num = random.randrange(0,5)
            word_index.append(num)
            list.append(word_board[word_index[i]].name)
        
        quiz_word = QUIZ
        for i in range(0,len(list)):
            quiz_word(question = word_board[i].meaning , one = list[0], two = list[1], three = list[2], four = list[3], five=list[4], answer = word_board[i].name).save()


        quiz_data =quiz_word.objects.all()

        if quiz_data:
            quiz_board = quiz_data.order_by('-id')[:5]

            res_data={
            "random_choice": quiz_board,
            "random_js": serializers.serialize('json',quiz_board),
            }

            return render(request, 'word/quiz.html',res_data)
        else:
            print("no data")
            return redirect('/word/list')

        
    else:
        return redirect('/word/list')
