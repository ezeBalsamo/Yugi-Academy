from .instance_creation_failed import InstanceCreationFailed


def enforce_not_blank(string, name):
    if not string.strip():
        raise InstanceCreationFailed(f'{name} must not be blank.')


def enforce_must_be_between(lower_bound, number_to_compare, upper_bound, number_name):
    if not (lower_bound <= number_to_compare <= upper_bound):
        raise InstanceCreationFailed(f'{number_name} must be between {lower_bound} and {upper_bound}.')
