from dependency_injector import containers, providers

from apps.rocket.container import RocketContainer


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    rocket_package = providers.Container(
        RocketContainer,
        config=config,
    )
