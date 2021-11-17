from django.urls import path
import word.views

app_name = "word"

urlpatterns =[
    path("list",word.views.list, name = "list")

]

