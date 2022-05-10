from django.db import models

# # Create your models here.
class WORD(models.Model):
    name = models.CharField(max_length=200, verbose_name="단어명")
    meaning = models.CharField(max_length=500, verbose_name="단어뜻")
    id = models.AutoField(primary_key=True)
    quiz = models.BooleanField(default = False)

    class Meta:
        db_table = "WORD_board"
