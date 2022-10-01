import collections

from .exceptions import InstanceCreationFailed


def enforce_not_blank(string, name):
    if not string.strip():
        raise InstanceCreationFailed(f'{name} must not be blank.')


def enforce_must_be_between(lower_bound, number_to_compare, upper_bound, number_name):
    if not (lower_bound <= number_to_compare <= upper_bound):
        raise InstanceCreationFailed(f'{number_name} must be between {lower_bound} and {upper_bound}.')


def enforce_must_be_positive_or_zero(number, number_name):
    if number < 0:
        raise InstanceCreationFailed(f'{number_name} must be positive.')


def with_the_only_one_in(collection, closure):
    assert len(collection) == 1
    closure(collection[0])


def assert_the_only_one_in(collection, expected_element):
    def assert_equals(element, another_element):
        assert element == another_element

    with_the_only_one_in(collection, lambda found_element: assert_equals(found_element, expected_element))


def assert_is_empty(collection):
    assert not collection


def assert_collections_have_same_elements(collection, another_collection):
    assert collections.Counter(collection) == collections.Counter(another_collection)


def enforce_is_included_in(element, name, collection):
    if element not in collection:
        raise InstanceCreationFailed(f'{name} must be one of this: {", ".join(collection)}.')
