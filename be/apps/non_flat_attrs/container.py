from dependency_injector import containers, providers

from helpers.models.non_flat_attrs import Node as NonFlatAttrsModel
from helpers.schemas.non_flat_attrs.schema import NonFlatAttrsNodeSchema

from . import entity, repository, service


class NonFlatAttrsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    non_flat_attrs_factory = providers.Factory(entity.NonFlatAttrsFactory)

    non_flat_attrs_repository = providers.Singleton(
        repository.NonFlatAttrsRepository,
        model=NonFlatAttrsModel,
        factory=non_flat_attrs_factory,
        schema=NonFlatAttrsNodeSchema,
        config=config,
    )

    non_flat_attrs_service = providers.Singleton(
        service.NonFlatAttrsService,
        repository=non_flat_attrs_repository,
    )
