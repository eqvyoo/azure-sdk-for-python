# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from typing import List, Mapping, Optional, Union, Any  # pylint: disable=unused-import
from enum import Enum, EnumMeta
from six import with_metaclass
from ._generated.models import EventSubscriptionType, MediaType
from ._shared.models import PhoneNumberIdentifier

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse # type: ignore

try:
    from typing import Protocol, TypedDict
except ImportError:
    from typing_extensions import Protocol, TypedDict
from azure.core import CaseInsensitiveEnumMeta

class CallLocatorKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Call Locator Kind."""

    GROUP_CALL_LOCATOR = "group_call_locator"
    SERVER_CALL_LOCATOR = "server_call_locator"

class CallLocator(object):
    """Call Locator.

    :ivar kind: The type of locator.
    :vartype kind: str or CallLocatorKind
    :ivar Mapping[str, Any] properties: The properties of the locator.
    """
    kind = None  # type: Optional[Union[CallLocatorKind, str]]
    properties = {}  # type: Mapping[str, Any]

GroupCallProperties = TypedDict(
    'GroupCallProperties',
    id=str
)

class GroupCallLocator(CallLocator):
    """The group call locator.

    :ivar kind: The type of locator.
    :vartype kind: str or CallLocatorKind
    :ivar Mapping[str, Any] properties: The properties of the locator.
     The keys in this mapping include:
        - `id`(str): ID of the Call.

    :param str id: ID of the Call.

    :ivar id: Required. The group call id.
    :type id: str
    """
    kind = CallLocatorKind.GROUP_CALL_LOCATOR

    def __init__(self, id):
        # type: (str) -> None
        if not id:
            raise ValueError("id can not be None or empty")

        self.properties = GroupCallProperties(id=id)

ServerCallProperties = TypedDict(
    'ServerCallProperties',
    id=str
)

class ServerCallLocator(CallLocator):
    """The server call locator.

    :ivar kind: The type of locator.
    :vartype kind: str or CallLocatorKind
    :ivar Mapping[str, Any] properties: The properties of the locator.
     The keys in this mapping include:
        - `id`(str): ID of the Call.

    :param str id: ID of the Call.

    :ivar id: Required. The server call id.
    :type id: str
    """
    kind = CallLocatorKind.SERVER_CALL_LOCATOR

    def __init__(self, id):
        # type: (str) -> None
        if not id:
            raise ValueError("id can not be None or empty")

        self.properties = ServerCallProperties(id=id)

class CreateCallOptions(object):
    """The options for creating a call.

    All required parameters must be populated in order to send to Azure.

    :ivar callback_uri: Required. The callback URI.
    :type callback_uri: str
    :ivar requested_media_types: The requested media types.
    :type requested_media_types: list[str or ~azure.communication.callingserver.models.MediaType]
    :ivar requested_call_events: The requested call events to subscribe to.
    :type requested_call_events: list[str or
     ~azure.communication.callingserver.models.EventSubscriptionType]
    """
    def __init__(
        self,
        callback_uri,  # type: str
        requested_media_types,  # type: List[MediaType]
        requested_call_events  # type: List[EventSubscriptionType]
    ):  # type: (...) -> None
        try:
            if not callback_uri.lower().startswith('http'):
                callback_uri = "https://" + callback_uri
        except AttributeError:
            raise ValueError("Host URL must be a string")

        parsed_url = urlparse(callback_uri.rstrip('/'))
        if not parsed_url.netloc:
            raise ValueError("Invalid URL: {}".format(callback_uri))

        if not requested_media_types:
            raise ValueError("requestedMediaTypes can not be None or empty")

        if not requested_call_events:
            raise ValueError("requestedCallEvents can not be None or empty")

        self.__callback_uri = callback_uri
        self.__requested_media_types = requested_media_types
        self.__requested_call_events = requested_call_events
        self.__alternate_Caller_Id = None
        self.__subject = None

    @property
    def callback_uri(self):
        # type: () -> Optional[str]
        return self.__callback_uri

    @property
    def requested_media_types(self):
        # type: () -> Optional[str]
        return self.__requested_media_types

    @property
    def requested_call_events(self):
        # type: () -> List[EventSubscriptionType]
        return self.__requested_call_events

    @property
    def alternate_Caller_Id(self):
        # type: () -> Optional[PhoneNumberIdentifier]
        return self.__alternate_Caller_Id
    @alternate_Caller_Id.setter
    def alternate_Caller_Id(self, alternate_Caller_Id):
        # type: (PhoneNumberIdentifier) -> None
        self.__alternate_Caller_Id = alternate_Caller_Id

    @property
    def subject(self):
        # type: () -> Optional[str]
        return self.__subject
    @subject.setter
    def subject(self, subject):
        # type: (str) -> None
        self.__subject = subject

class JoinCallOptions(object):
    """The options for joining a call.

    All required parameters must be populated in order to send to Azure.

    :ivar callback_uri: Required. The callback URI.
    :type callback_uri: str
    :ivar requested_media_types: The requested media types.
    :type requested_media_types: list[str or ~azure.communication.callingserver.models.MediaType]
    :ivar requested_call_events: The requested call events to subscribe to.
    :type requested_call_events: list[str or
     ~azure.communication.callingserver.models.EventSubscriptionType]
    """
    def __init__(
        self,
        callback_uri,  # type: str
        requested_media_types,  # type: List[MediaType]
        requested_call_events  # type: List[EventSubscriptionType]
    ):  # type: (...) -> None
        try:
            if not callback_uri.lower().startswith('http'):
                callback_uri = "https://" + callback_uri
        except AttributeError:
            raise ValueError("Host URL must be a string")

        parsed_url = urlparse(callback_uri.rstrip('/'))
        if not parsed_url.netloc:
            raise ValueError("Invalid URL: {}".format(callback_uri))

        if not requested_media_types:
            raise ValueError("requestedMediaTypes can not be None or empty")

        if not requested_call_events:
            raise ValueError("requestedCallEvents can not be None or empty")

        self.__callback_uri = callback_uri
        self.__requested_media_types = requested_media_types
        self.__requested_call_events = requested_call_events
        self.__subject = None

    @property
    def callback_uri(self):
        # type: () -> str
        return self.__callback_uri

    @property
    def requested_media_types(self):
        # type: () -> List[MediaType]
        return self.__requested_media_types

    @property
    def requested_call_events(self):
        # type: () -> List[EventSubscriptionType]
        return self.__requested_call_events

    @property
    def subject(self):
        # type: () -> Optional[str]
        return self.__subject
    @subject.setter
    def subject(self, subject):
        # type: (str) -> None
        self.__subject = subject

class PlayAudioOptions(object):
    """The options for playing audio.

    All required parameters must be populated in order to send to Azure.

    :ivar loop: Required. The flag indicating whether audio file needs to be played in loop or not.
    :type loop: bool
    :ivar operation_context: Required. The value to identify context of the operation.
    :type operation_context: str
    :ivar audio_file_id: Required. An id for the media in the AudioFileUri, using which we cache the media resource.
    :type audio_file_id: str
    :ivar callback_uri: Required. The callback Uri to receive PlayAudio status notifications.
    :type callback_uri: str
    """
    def __init__(
        self,
        loop,  # type: bool
        operation_context,  # type: str
        audio_file_id,  # type: str
        callback_uri  # type: str
    ):  # type: (...) -> None
        self.loop = loop
        self.operation_context = operation_context
        self.audio_file_id = audio_file_id
        self.callback_uri = callback_uri
        self.__subject = None

    @property
    def subject(self):
        # type: () -> Optional[str]
        return self.__subject
    @subject.setter
    def subject(self, subject):
        # type: (str) -> None
        self.__subject = subject