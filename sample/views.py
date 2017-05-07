from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework_auth0.permissions import HasAdminRole
from rest_framework_auth0.views import GroupsQuerysetFilterMixin


class ToDoViewSet(GroupsQuerysetFilterMixin, viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = (HasAdminRole, )
