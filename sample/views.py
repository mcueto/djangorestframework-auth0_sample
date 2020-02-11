from rest_framework import (
    viewsets,
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework_auth0.authentication import (
    Auth0JSONWebTokenAuthentication,
)
from rest_framework_auth0.permissions import (
    HasAdminRole,
)
from rest_framework_auth0.views import (
    GroupsQuerysetFilterMixin,
)
from .models import (
    ToDo,
)
from .serializers import (
    ToDoSerializer,
)
from .permissions import (
    HasAdminGroupPermission,
)


class AllToDosViewSet(viewsets.ModelViewSet):
    """
    AllToDosViewSet.
    Retrieve a list with all ToDo model instances.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class SecureToDosViewSet(viewsets.ModelViewSet):
    """
    SecureToDosViewSet.
    Retrieve a list with all ToDo model instances only when the user is
    authenticated.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


class AdminToDosViewSet(viewsets.ModelViewSet):
    """
    AdminToDosViewSet.
    Retrieve a list with all ToDo model instances only when the user is
    authenticated and has admin group permissions.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [HasAdminGroupPermission]


class ToDoViewSet(GroupsQuerysetFilterMixin, viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = (HasAdminRole, )
