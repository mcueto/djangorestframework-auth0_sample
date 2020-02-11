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


class MyOwnToDosViewSet(viewsets.ModelViewSet):
    """
    MyOwnToDosViewSet.
    Retrieve a list with all ToDo model instances only to the user is
    authenticated.
    """
    serializer_class = ToDoSerializer
    authentication_classes = [Auth0JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get ToDos for the authenticated User.

        This view should return a list of all the ToDos for the currently
        authenticated user.
        """
        user = self.request.user

        return ToDo.objects.filter(
            user=user
        )

    # When a ToDo is created on this endpoint, associate the user so it can
    # be filtered later
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class ToDoViewSet(GroupsQuerysetFilterMixin, viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = (HasAdminRole, )
