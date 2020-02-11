from rest_framework_auth0.permissions import(
    HasGroupBasePermission,
    HasRoleBasePermission,
    HasPermissionBasePermission,
)


# Custom permissions
class HasAdminGroupPermission(HasGroupBasePermission):
    group_name = 'todos_admins'


class HasAdminRolePermission(HasRoleBasePermission):
    role_name = 'admin'


class CanReadToDosPermission(HasPermissionBasePermission):
    permission_name = 'read:todos'
