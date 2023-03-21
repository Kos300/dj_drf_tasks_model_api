from rest_framework import serializers
from .models import Todo


# Todo serializer
# описываем что все поля модели Todo
# нужно сериализовать в json
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'