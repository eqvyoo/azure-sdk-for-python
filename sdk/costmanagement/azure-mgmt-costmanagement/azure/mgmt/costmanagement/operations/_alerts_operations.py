# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AlertsOperations(object):
    """AlertsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.costmanagement.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        scope,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AlertsResult"
        """Lists the alerts for scope defined.

        :param scope: The scope associated with alerts operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertsResult, or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.AlertsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AlertsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-11-01"
        accept = "application/json"

        # Construct URL
        url = self.list.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AlertsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/alerts'}  # type: ignore

    def get(
        self,
        scope,  # type: str
        alert_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Alert"
        """Gets the alert for the scope by alert ID.

        :param scope: The scope associated with alerts operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param alert_id: Alert ID.
        :type alert_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Alert, or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.Alert
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Alert"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-11-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'alertId': self._serialize.url("alert_id", alert_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Alert', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/alerts/{alertId}'}  # type: ignore

    def dismiss(
        self,
        scope,  # type: str
        alert_id,  # type: str
        parameters,  # type: "_models.DismissAlertPayload"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Alert"
        """Dismisses the specified alert.

        :param scope: The scope associated with alerts operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param alert_id: Alert ID.
        :type alert_id: str
        :param parameters: Parameters supplied to the Dismiss Alert operation.
        :type parameters: ~azure.mgmt.costmanagement.models.DismissAlertPayload
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Alert, or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.Alert
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Alert"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-11-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.dismiss.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
            'alertId': self._serialize.url("alert_id", alert_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'DismissAlertPayload')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Alert', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    dismiss.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/alerts/{alertId}'}  # type: ignore

    def list_external(
        self,
        external_cloud_provider_type,  # type: Union[str, "_models.ExternalCloudProviderType"]
        external_cloud_provider_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AlertsResult"
        """Lists the Alerts for external cloud provider type defined.

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account.
        :type external_cloud_provider_type: str or ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
        :type external_cloud_provider_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertsResult, or the result of cls(response)
        :rtype: ~azure.mgmt.costmanagement.models.AlertsResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AlertsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-11-01"
        accept = "application/json"

        # Construct URL
        url = self.list_external.metadata['url']  # type: ignore
        path_format_arguments = {
            'externalCloudProviderType': self._serialize.url("external_cloud_provider_type", external_cloud_provider_type, 'str'),
            'externalCloudProviderId': self._serialize.url("external_cloud_provider_id", external_cloud_provider_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AlertsResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_external.metadata = {'url': '/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/alerts'}  # type: ignore
