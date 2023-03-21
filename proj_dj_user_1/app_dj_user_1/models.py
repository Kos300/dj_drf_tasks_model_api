from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400, blank=True)
    # дата создания
    date = models.DateTimeField(auto_now_add=True)
    # флаг - выполнена ли задача
    done = models.BooleanField(default=False, null=False)
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    # строковое представление по названию
    def __str__(self):
        return self.title
