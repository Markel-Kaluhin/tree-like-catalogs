from apps.container import Container
from apps.rocket import controller as rocket_controller
from settings.base import settings


def wire_container() -> Container:
    container = Container()
    container.init_resources()
    container.config.from_value(settings)
    container.wire(
        modules=[
            rocket_controller,
        ]
    )
    return container
