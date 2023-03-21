from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


# Todo ViewSet
# определим queryset, как объекты Todo в БД.
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer