import unittest
from datetime import datetime, timezone
from decimal import Decimal
from unittest.mock import MagicMock, AsyncMock

from apps.non_flat_attrs.entity import NonFlatAttrsFactory
from apps.non_flat_attrs.repository import NonFlatAttrsRepository
from apps.non_flat_attrs.service import NonFlatAttrsService
from helpers.exceptions.base import NonFlatAttrsException
from helpers.schemas.non_flat_attrs.schema import (
    NonFlatAttrsNodeSchema,
    NonFlatAttrsPropertySchema,
)


class TestNonFlatAttrsService(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.mock_repository = MagicMock(spec=NonFlatAttrsRepository)
        self.mock_repository.factory = MagicMock(spec=NonFlatAttrsFactory)
        self.service = NonFlatAttrsService(self.mock_repository)

    async def test_get_tree_node_and_property_exist(self):
        self.mock_repository.get_latest_node_id = AsyncMock(
            return_value=(1, 2, 3)
        )
        self.mock_repository.get_property_by_latest_node_id = AsyncMock(
            return_value=NonFlatAttrsPropertySchema(
                name="Test node",
                value=Decimal(30.155),
                created_at=datetime.now()
            )
        )
        self.mock_repository.get_node_list_by_node_id = AsyncMock(return_value=[])
        self.mock_repository.factory.serialize = MagicMock(return_value=NonFlatAttrsNodeSchema(id=1, name="Test node", created_at=datetime.now()))
        result = await self.service.get_tree("route_path")
        self.assertIsInstance(result, NonFlatAttrsNodeSchema)

    async def test_get_tree_node_or_property_does_not_exist(self):
        self.mock_repository.get_latest_node_id = AsyncMock(
            return_value=(None, None, None)
        )
        self.mock_repository.get_property_by_latest_node_id = AsyncMock(
            return_value=None
        )
        with self.assertRaises(NonFlatAttrsException):
            await self.service.get_tree("route_path")

    async def test_create_node_already_exists(self):
        self.mock_repository.get_latest_node_id = AsyncMock(
            return_value=(1, 0, 0)
        )
        with self.assertRaises(NonFlatAttrsException):
            await self.service.create("route_path", None)

    async def test_create_successful(self):
        self.mock_repository.get_latest_node_id = AsyncMock(
            return_value=(1, 1, 1)
        )
        self.mock_repository.create_node = AsyncMock(
            return_value=NonFlatAttrsNodeSchema(id=1, name="Test node", created_at=datetime.now())
        )
        result = await self.service.create("route_path", None)
        self.assertIsInstance(result, NonFlatAttrsNodeSchema)

    async def test_delete_node_successful(self):
        self.mock_repository.get_node_list_by_node_id = AsyncMock(
            return_value=[(3, 1, 'Cylinder Head',
                           datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc),
                           datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc), 6, 3,
                           'Intake Valve Diameter', Decimal('32'),
                           datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc),
                           datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc)), (
                              3, 1, 'Cylinder Head',
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc),
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc), 7, 3,
                              'Exhaust Valve Diameter', Decimal('28'),
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc),
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc)), (
                              10, 3, 'Valves',
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc),
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc), None, None,
                              None, None, None, None), (11, 3, 'Valve Guides',
                                                        datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                 tzinfo=timezone.utc),
                                                        datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                 tzinfo=timezone.utc), None, None, None,
                                                        None, None, None), (12, 3, 'Piston Head',
                                                                            datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                                     tzinfo=timezone.utc),
                                                                            datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                                     tzinfo=timezone.utc),
                                                                            None, None, None, None, None, None), (
                              13, 3, 'Camshaft',
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc),
                              datetime(2023, 9, 24, 4, 2, 23, 994613, tzinfo=timezone.utc), None, None,
                              None, None, None, None), (14, 3, 'Thermostat',
                                                        datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                 tzinfo=timezone.utc),
                                                        datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                 tzinfo=timezone.utc), None, None, None,
                                                        None, None, None), (15, 3, 'Cylinder Head Gasket',
                                                                            datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                                     tzinfo=timezone.utc),
                                                                            datetime(2023, 9, 24, 4, 2, 23, 994613,
                                                                                     tzinfo=timezone.utc),
                                                                            None, None, None, None, None, None)]
        )
        self.mock_repository.delete_property = AsyncMock()
        self.mock_repository.delete_node = AsyncMock()
        await self.service.delete_node(1)
        self.mock_repository.delete_property.assert_called_once_with(property_id_list=[6, 7])
        self.mock_repository.delete_node.assert_called_once_with(node_id_list=[3, 10, 11, 12, 13, 14, 15])

    async def test_delete_property_successful(self):
        self.mock_repository.delete_property = AsyncMock()
        await self.service.delete_property(1)
        self.mock_repository.delete_property.assert_called_once_with(property_id_list=[1])
