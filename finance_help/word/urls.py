from django.urls import path
import word.views
import pandas as pd
import random

app_name = "word"

urlpatterns =[
    path("list",word.views.list, name = "list")

]

