from django.urls import path
from django.contrib import admin
import word.views
import pandas as pd
import random

app_name = "word"

urlpatterns =[
    path("list",word.views.list, name = "list"),
    path("quiz",word.views.quiz, name="quiz"),
    path("result",word.views.result, name="result"),
]

