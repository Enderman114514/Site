from django.db import models

# Create your models here.

class Comment(models.Model):
    owner = models.CharField(max_length=15, verbose_name="昵称")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="日期")
    content = models.CharField(max_length=150, verbose_name="留言")

    def __str__(self):
        return self.content