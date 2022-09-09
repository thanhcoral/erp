from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


def group_required(*group_names, login_url=None, raise_exception=False):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        if raise_exception:
            raise PermissionDenied
        return False

    return user_passes_test(in_groups, login_url=login_url)