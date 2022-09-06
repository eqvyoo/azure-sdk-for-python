# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import ServiceBusManagementClientConfiguration
from .operations import DisasterRecoveryConfigsOperations, MigrationConfigsOperations, NamespacesOperations, Operations, PrivateEndpointConnectionsOperations, PrivateLinkResourcesOperations, QueuesOperations, RulesOperations, SubscriptionsOperations, TopicsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class ServiceBusManagementClient:    # pylint: disable=too-many-instance-attributes
    """Azure Service Bus client for managing Namespace.

    :ivar namespaces: NamespacesOperations operations
    :vartype namespaces: azure.mgmt.servicebus.v2021_11_01.operations.NamespacesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.servicebus.v2021_11_01.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.servicebus.v2021_11_01.operations.PrivateLinkResourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.servicebus.v2021_11_01.operations.Operations
    :ivar disaster_recovery_configs: DisasterRecoveryConfigsOperations operations
    :vartype disaster_recovery_configs:
     azure.mgmt.servicebus.v2021_11_01.operations.DisasterRecoveryConfigsOperations
    :ivar migration_configs: MigrationConfigsOperations operations
    :vartype migration_configs:
     azure.mgmt.servicebus.v2021_11_01.operations.MigrationConfigsOperations
    :ivar queues: QueuesOperations operations
    :vartype queues: azure.mgmt.servicebus.v2021_11_01.operations.QueuesOperations
    :ivar topics: TopicsOperations operations
    :vartype topics: azure.mgmt.servicebus.v2021_11_01.operations.TopicsOperations
    :ivar rules: RulesOperations operations
    :vartype rules: azure.mgmt.servicebus.v2021_11_01.operations.RulesOperations
    :ivar subscriptions: SubscriptionsOperations operations
    :vartype subscriptions: azure.mgmt.servicebus.v2021_11_01.operations.SubscriptionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2021-11-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ServiceBusManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.namespaces = NamespacesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.disaster_recovery_configs = DisasterRecoveryConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.migration_configs = MigrationConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.queues = QueuesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.topics = TopicsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.rules = RulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.subscriptions = SubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ServiceBusManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
