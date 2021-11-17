from django.shortcuts import render


def list(request,crawling):
    return render(request, 'word/word_base.html')