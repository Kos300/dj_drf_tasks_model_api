from django.contrib import admin
from .models import Todo, Category

# Register your models here.

# опишем что будет видно в админке при работе с моделью
class TodoAdmin(admin.ModelAdmin):
    # видимые поля в списке
    list_display = ('id', 'title', 'category', 'description', 'date', 'done')
    list_display_links = ('id', 'title')
    # по каким полям искать
    search_fields = ('id', 'title', 'description', )
    # какие поля изменять из списка не входя в карточку
    list_editable = ('done', 'category',)
    # по каким параметрам можем фильтровать
    list_filter = ('done', 'date', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)