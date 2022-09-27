from django.core.exceptions import ObjectDoesNotExist

from assertions import SystemRestrictionInfringed


def raise_not_found_managed_object_in(repository, query_filter):
    raise SystemRestrictionInfringed(f'There is no {repository.model.type_description} matching {query_filter}.')


def managed_object_filtered_by(query_filter, repository, if_found=None, if_none=None):
    try:
        managed_object = repository.get(**query_filter)
        return managed_object if if_found is None else if_found(managed_object)
    except ObjectDoesNotExist:
        raise_not_found_managed_object_in(repository, query_filter) if if_none is None else if_none()