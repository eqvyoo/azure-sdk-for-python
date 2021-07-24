# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class EntitiesOperations:
    """EntitiesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.managementgroups.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        skiptoken: Optional[str] = None,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        select: Optional[str] = None,
        search: Optional[Union[str, "_models.Enum2"]] = None,
        filter: Optional[str] = None,
        view: Optional[Union[str, "_models.Enum3"]] = None,
        group_name: Optional[str] = None,
        cache_control: Optional[str] = "no-cache",
        **kwargs: Any
    ) -> AsyncIterable["_models.EntityListResult"]:
        """List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.

        :param skiptoken: Page continuation token is only used if a previous operation returned a
         partial result.
         If a previous response contains a nextLink element, the value of the nextLink element will
         include a token parameter that specifies a starting point to use for subsequent calls.
        :type skiptoken: str
        :param skip: Number of entities to skip over when retrieving results. Passing this in will
         override $skipToken.
        :type skip: int
        :param top: Number of elements to return when retrieving results. Passing this in will override
         $skipToken.
        :type top: int
        :param select: This parameter specifies the fields to include in the response. Can include any
         combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g.
         '$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain'. When specified the
         $select parameter can override select in $skipToken.
        :type select: str
        :param search: The $search parameter is used in conjunction with the $filter parameter to
         return three different outputs depending on the parameter passed in.
         With $search=AllowedParents the API will return the entity info of all groups that the
         requested entity will be able to reparent to as determined by the user's permissions.
         With $search=AllowedChildren the API will return the entity info of all entities that can be
         added as children of the requested entity.
         With $search=ParentAndFirstLevelChildren the API will return the parent and  first level of
         children that the user has either direct access to or indirect access via one of their
         descendants.
         With $search=ParentOnly the API will return only the group if the user has access to at least
         one of the descendants of the group.
         With $search=ChildrenOnly the API will return only the first level of children of the group
         entity info specified in $filter.  The user must have direct access to the children entities or
         one of it's descendants for it to show up in the results.
        :type search: str or ~azure.mgmt.managementgroups.models.Enum2
        :param filter: The filter parameter allows you to filter on the the name or display name
         fields. You can check for equality on the name field (e.g. name eq '{entityName}')  and you can
         check for substrings on either the name or display name fields(e.g. contains(name,
         '{substringToSearch}'), contains(displayName, '{substringToSearch')). Note that the
         '{entityName}' and '{substringToSearch}' fields are checked case insensitively.
        :type filter: str
        :param view: The view parameter allows clients to filter the type of data that is returned by
         the getEntities call.
        :type view: str or ~azure.mgmt.managementgroups.models.Enum3
        :param group_name: A filter which allows the get entities call to focus on a particular group
         (i.e. "$filter=name eq 'groupName'").
        :type group_name: str
        :param cache_control: Indicates whether the request should utilize any caches. Populate the
         header with 'no-cache' value to bypass existing caches.
        :type cache_control: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either EntityListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.managementgroups.models.EntityListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EntityListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-04-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            if cache_control is not None:
                header_parameters['Cache-Control'] = self._serialize.header("cache_control", cache_control, 'str')
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if skiptoken is not None:
                    query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')
                if skip is not None:
                    query_parameters['$skip'] = self._serialize.query("skip", skip, 'int')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')
                if search is not None:
                    query_parameters['$search'] = self._serialize.query("search", search, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if view is not None:
                    query_parameters['$view'] = self._serialize.query("view", view, 'str')
                if group_name is not None:
                    query_parameters['groupName'] = self._serialize.query("group_name", group_name, 'str')

                request = self._client.post(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('EntityListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/providers/Microsoft.Management/getEntities'}  # type: ignore