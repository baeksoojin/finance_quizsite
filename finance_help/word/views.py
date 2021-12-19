from django.db import reset_queries
from django.shortcuts import render, redirect
import random
import sys
sys.path.append('C:\\project\\finance\\finance_help\\word')
from get_data import get_data
from word.models import WORD

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
    # data = get_data() # 사용자가 요청할 때만 get_data()를 호출해야할 필요성이 있음.

    # res_data ={}
    # res_data['data']=data

    return render(request, 'word/word_list.html',res_data)



def quiz(request):

    if request.method == "POST":
        word = WORD

        all_word_board = word.objects.all()
        res_data={}
        res_data['random_choice'] = all_word_board.order_by('-id')[:5]

        return render(request, 'word/quiz.html',res_data)
    else:
        return redirect('/word/list')
