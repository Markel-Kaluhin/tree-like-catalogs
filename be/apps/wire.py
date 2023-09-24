from apps.container import Container
from apps.non_flat_attrs import controller as non_flat_attrs_controller
from settings.base import settings


def wire_container() -> Container:
    container = Container()
    container.init_resources()
    container.config.from_value(settings)
    container.wire(
        modules=[
            non_flat_attrs_controller,
        ]
    )
    return container
