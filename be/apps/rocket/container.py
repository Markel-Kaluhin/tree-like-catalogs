from dependency_injector import containers, providers

from helpers.models.rocket import RocketNode as RocketModel
from helpers.schemas.rocket.schema import RocketNodeSchema

from . import entity, repository, service


class RocketContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    rocket_factory = providers.Factory(entity.RocketFactory)

    rocket_repository = providers.Singleton(
        repository.RocketRepository,
        model=RocketModel,
        factory=rocket_factory,
        schema=RocketNodeSchema,
        config=config,
    )

    rocket_service = providers.Singleton(
        service.RocketService,
        repository=rocket_repository,
    )
