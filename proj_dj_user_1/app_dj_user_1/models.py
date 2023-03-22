from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=400, blank=True)
    # дата создания
    date = models.DateTimeField(auto_now_add=True)
    # флаг - выполнена ли задача
    done = models.BooleanField(default=False, null=False)
        # PROTECT - при удалении Категории предлагает удалить связанные Задачи
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
        # DO_NOTHING - позволяет удалить Категорию, но если есть связанные Задачи то выдает ошибку
    # category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True)
        # SET_DEFAULT - добавил default=None, при удалении Категории в связанных Задачах изменит значение на дефолтное.
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, null=True, blank=True, default=None)

    # строковое представление по названию
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

