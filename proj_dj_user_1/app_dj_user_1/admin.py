from django.contrib import admin
from .models import Todo

# Register your models here.

# опишем что будет видно в админке при работе с моделью
class TodoAdmin(admin.ModelAdmin):
    # видимые поля в списке
    list_display = ('id', 'title',  'description', 'date', 'done')
    list_display_links = ('id', 'title')
    # по каким полям искать
    search_fields = ('id', 'title')
    # какие поля изменять из списка не входя в карточку
    list_editable = ('done',)
    # по каким параметрам можем фильтровать
    list_filter = ('done', 'date', )

admin.site.register(Todo, TodoAdmin)
