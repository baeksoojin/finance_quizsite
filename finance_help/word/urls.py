from django.urls import path
from django.contrib import admin
import word.views
import pandas as pd
import random

app_name = "word"

urlpatterns =[
    path("list",word.views.list, name = "list"),
    path("reset",word.views.reset,name="reset"),
    path("quiz",word.views.quiz, name="quiz"),
]

