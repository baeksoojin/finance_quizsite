from django.db import models

# # Create your models here.
class WORD(models.Model):
    name = models.CharField(max_length=200, verbose_name="단어명")
    meaning = models.CharField(max_length=500, verbose_name="단어뜻")
    id = models.AutoField(primary_key=True)


    class Meta:
        db_table = "WORD_board"

class QUIZ(models.Model):
    question = models.CharField(max_length=200, verbose_name="퀴즈")
    one = models.CharField(max_length=30, verbose_name="보기1")
    two = models.CharField(max_length=30, verbose_name="보기2")
    three = models.CharField(max_length=30, verbose_name="보기3")
    four = models.CharField(max_length=30, verbose_name="보기4")
    five = models.CharField(max_length=30, verbose_name="보기5")
    answer = models.CharField(max_length=30, verbose_name = "정답")

    class Meta:
        db_table = "QUIZ_board"