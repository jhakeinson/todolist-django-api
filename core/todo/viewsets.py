import email
from core.todo.serializers import TodoSerializer
from core.todo.models import Todo
from core.user.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        user = User.objects.get(email=self.request.user.email)
        print('user: ', user)
        if user.is_superuser:
            return Todo.objects.all()
        else:
            return Todo.objects.filter(user=self.request.user)

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = Todo.objects.get(pk=lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
    
    def destroy(self, request, *args, **kwargs):
        print('destroy')
        return super().destroy(request, *args, **kwargs)