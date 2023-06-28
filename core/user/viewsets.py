from core.user.serializers import UserSerializer
from core.user.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    ordering = ['-updated']

    def get_queryset(self):
        print('user: ', self.request.user)
        if self.request.user.is_superuser:
            # return all users
            return User.objects.all()
        else:
            # return not permitted to access
            return User.objects.none()

    def get_object(self):
        print('lookup_field: ', self.lookup_field)
        print('kwargs: ', self.kwargs)
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(pk=lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj