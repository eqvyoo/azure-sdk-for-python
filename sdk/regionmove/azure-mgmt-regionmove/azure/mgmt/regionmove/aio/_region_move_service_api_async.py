# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import RegionMoveServiceAPIConfiguration
from .operations_async import MoveCollectionsOperations
from .operations_async import MoveResourcesOperations
from .operations_async import UnresolvedDependenciesOperations
from .operations_async import OperationsDiscoveryOperations
from .. import models


class RegionMoveServiceAPI(object):
    """A first party Azure service orchestrating the move of Azure resources from one Azure region to another or between zones within a region.

    :ivar move_collections: MoveCollectionsOperations operations
    :vartype move_collections: region_move_service_api.aio.operations_async.MoveCollectionsOperations
    :ivar move_resources: MoveResourcesOperations operations
    :vartype move_resources: region_move_service_api.aio.operations_async.MoveResourcesOperations
    :ivar unresolved_dependencies: UnresolvedDependenciesOperations operations
    :vartype unresolved_dependencies: region_move_service_api.aio.operations_async.UnresolvedDependenciesOperations
    :ivar operations_discovery: OperationsDiscoveryOperations operations
    :vartype operations_discovery: region_move_service_api.aio.operations_async.OperationsDiscoveryOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = RegionMoveServiceAPIConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.move_collections = MoveCollectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.move_resources = MoveResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.unresolved_dependencies = UnresolvedDependenciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations_discovery = OperationsDiscoveryOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "RegionMoveServiceAPI":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)