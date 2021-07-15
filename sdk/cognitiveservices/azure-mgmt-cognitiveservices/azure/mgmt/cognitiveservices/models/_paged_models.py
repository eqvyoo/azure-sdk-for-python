# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class AccountPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Account <azure.mgmt.cognitiveservices.models.Account>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Account]'}
    }

    def __init__(self, *args, **kwargs):

        super(AccountPaged, self).__init__(*args, **kwargs)
class ResourceSkuPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ResourceSku <azure.mgmt.cognitiveservices.models.ResourceSku>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ResourceSku]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourceSkuPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.cognitiveservices.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)