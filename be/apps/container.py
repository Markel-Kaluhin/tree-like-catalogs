from dependency_injector import containers, providers

from apps.non_flat_attrs.container import NonFlatAttrsContainer


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    non_flat_attrs_package = providers.Container(
        NonFlatAttrsContainer,
        config=config,
    )
