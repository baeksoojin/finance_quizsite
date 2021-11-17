from django.shortcuts import render
import random
import sys
sys.path.append('C:\\project\\finance\\finance_help\\word')

from get_data import get_data

# def test():
#     #get_data함수에 대한 test
#     print("test중\n",get_data())

# test()

def list(request):

    data = get_data()
    res_data ={}
    res_data['data']=data


    return render(request, 'word/word_list.html',res_data)