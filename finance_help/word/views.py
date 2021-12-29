from django.db import reset_queries
from django.shortcuts import render, redirect
import random
import sys
sys.path.append('C:\\project\\finance\\finance_help\\word')
from get_data import get_data
from word.models import WORD,QUIZ


# def test():
#     #get_data함수에 대한 test
#     print("test중\n",get_data())

# test()

def reset(request):

    if request.method == "POST":
        data = get_data()

        word_board = WORD

        for i in range(0,len(data)):
            word_board(name = data[i][0], meaning = data[i][1]).save()

        return redirect("/word/list")

    else:
        render(request,'word/word_list.html')




def list(request):

        
    res_data={}
    word = WORD
    
    if not word.objects.all():
        data = get_data()
        for i in range(0,len(data)):
            word(name = data[i][0], meaning = data[i][1]).save()
    
    if word.objects.all():
        all_word_board = word.objects.all()
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
        for i in range(0,5):
            list.append(word_board[i].name)
        
        quiz_word = QUIZ
        for i in range(0,len(list)):
            quiz_word(question = word_board[i].meaning , one = list[0], two = list[1], three = list[2], four = list[3], five=list[4], answer = word_board[i].name).save()


        quiz_data =quiz_word.objects.all()

        if quiz_data:
            quiz_board = quiz_data.order_by('-id')[:1]

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
