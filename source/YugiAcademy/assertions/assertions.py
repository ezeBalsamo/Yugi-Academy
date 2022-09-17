from .instance_creation_failed import InstanceCreationFailed


def enforce_not_blank(string, name):
    if not string.strip():
        raise InstanceCreationFailed(f'{name} must not be blank.')
