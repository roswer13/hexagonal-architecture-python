from typing import Any, Dict
from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
    container: Dict[str, Any]

    def ready(self) -> None:
        from myapp.dependencies_container import build_production_dependencies_container
        self.container = build_production_dependencies_container()
