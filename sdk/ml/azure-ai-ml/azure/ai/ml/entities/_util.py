# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import copy
import hashlib
import json
import os
import shutil
from collections import OrderedDict
from typing import Any, Dict, List, Optional, Union
from unittest import mock

from marshmallow.exceptions import ValidationError

from azure.ai.ml._ml_exceptions import ErrorTarget, ValidationErrorType, ValidationException
from azure.ai.ml._schema._datastore import (
    AzureBlobSchema,
    AzureDataLakeGen1Schema,
    AzureDataLakeGen2Schema,
    AzureFileSchema,
)
from azure.ai.ml._schema._deployment.batch.batch_deployment import BatchDeploymentSchema
from azure.ai.ml._schema._deployment.online.online_deployment import (
    KubernetesOnlineDeploymentSchema,
    ManagedOnlineDeploymentSchema,
)
from azure.ai.ml._schema._endpoint.batch.batch_endpoint import BatchEndpointSchema
from azure.ai.ml._schema._endpoint.online.online_endpoint import (
    KubernetesOnlineEndpointSchema,
    ManagedOnlineEndpointSchema,
)
from azure.ai.ml._schema._sweep import SweepJobSchema
from azure.ai.ml._schema.assets.data import DataSchema
from azure.ai.ml._schema.assets.environment import EnvironmentSchema
from azure.ai.ml._schema.assets.model import ModelSchema
from azure.ai.ml._schema.component.command_component import CommandComponentSchema
from azure.ai.ml._schema.component.parallel_component import ParallelComponentSchema
from azure.ai.ml._schema.compute.aml_compute import AmlComputeSchema
from azure.ai.ml._schema.compute.compute_instance import ComputeInstanceSchema
from azure.ai.ml._schema.compute.virtual_machine_compute import VirtualMachineComputeSchema
from azure.ai.ml._schema.job import CommandJobSchema, ParallelJobSchema
from azure.ai.ml._schema.pipeline.pipeline_job import PipelineJobSchema
from azure.ai.ml._schema.schedule.schedule import ScheduleSchema
from azure.ai.ml._schema.workspace import WorkspaceSchema
from azure.ai.ml._utils.utils import camel_to_snake, snake_to_pascal
from azure.ai.ml.constants._common import (
    REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT,
    CommonYamlFields,
    YAMLRefDocLinks,
    YAMLRefDocSchemaNames,
)
from azure.ai.ml.constants._endpoint import EndpointYamlFields

# Maps schema class name to formatted error message pointing to Microsoft docs reference page for a schema's YAML
REF_DOC_ERROR_MESSAGE_MAP = {
    DataSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(YAMLRefDocSchemaNames.DATA, YAMLRefDocLinks.DATA),
    EnvironmentSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.ENVIRONMENT, YAMLRefDocLinks.ENVIRONMENT
    ),
    ModelSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(YAMLRefDocSchemaNames.MODEL, YAMLRefDocLinks.MODEL),
    CommandComponentSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.COMMAND_COMPONENT, YAMLRefDocLinks.COMMAND_COMPONENT
    ),
    ParallelComponentSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.PARALLEL_COMPONENT, YAMLRefDocLinks.PARALLEL_COMPONENT
    ),
    AmlComputeSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.AML_COMPUTE, YAMLRefDocLinks.AML_COMPUTE
    ),
    ComputeInstanceSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.COMPUTE_INSTANCE, YAMLRefDocLinks.COMPUTE_INSTANCE
    ),
    VirtualMachineComputeSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.VIRTUAL_MACHINE_COMPUTE,
        YAMLRefDocLinks.VIRTUAL_MACHINE_COMPUTE,
    ),
    AzureDataLakeGen1Schema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.DATASTORE_DATA_LAKE_GEN_1,
        YAMLRefDocLinks.DATASTORE_DATA_LAKE_GEN_1,
    ),
    AzureBlobSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.DATASTORE_BLOB, YAMLRefDocLinks.DATASTORE_BLOB
    ),
    AzureFileSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.DATASTORE_FILE, YAMLRefDocLinks.DATASTORE_FILE
    ),
    AzureDataLakeGen2Schema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.DATASTORE_DATA_LAKE_GEN_2,
        YAMLRefDocLinks.DATASTORE_DATA_LAKE_GEN_2,
    ),
    BatchEndpointSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.BATCH_ENDPOINT, YAMLRefDocLinks.BATCH_ENDPOINT
    ),
    KubernetesOnlineEndpointSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.ONLINE_ENDPOINT, YAMLRefDocLinks.ONLINE_ENDPOINT
    ),
    ManagedOnlineEndpointSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.ONLINE_ENDPOINT, YAMLRefDocLinks.ONLINE_ENDPOINT
    ),
    BatchDeploymentSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.BATCH_DEPLOYMENT, YAMLRefDocLinks.BATCH_DEPLOYMENT
    ),
    ManagedOnlineDeploymentSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.MANAGED_ONLINE_DEPLOYMENT,
        YAMLRefDocLinks.MANAGED_ONLINE_DEPLOYMENT,
    ),
    KubernetesOnlineDeploymentSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.KUBERNETES_ONLINE_DEPLOYMENT,
        YAMLRefDocLinks.KUBERNETES_ONLINE_DEPLOYMENT,
    ),
    PipelineJobSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.PIPELINE_JOB, YAMLRefDocLinks.PIPELINE_JOB
    ),
    ScheduleSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.SCHEDULE, YAMLRefDocLinks.SCHEDULE
    ),
    SweepJobSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.SWEEP_JOB, YAMLRefDocLinks.SWEEP_JOB
    ),
    CommandJobSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.COMMAND_JOB, YAMLRefDocLinks.COMMAND_JOB
    ),
    ParallelJobSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.PARALLEL_JOB, YAMLRefDocLinks.PARALLEL_JOB
    ),
    WorkspaceSchema: REF_DOC_YAML_SCHEMA_ERROR_MSG_FORMAT.format(
        YAMLRefDocSchemaNames.WORKSPACE, YAMLRefDocLinks.WORKSPACE
    ),
}


def find_type_in_override(params_override: list = None) -> Optional[str]:
    params_override = params_override or []
    for override in params_override:
        if CommonYamlFields.TYPE in override:
            return override[CommonYamlFields.TYPE]
    return None


def is_compute_in_override(params_override: list = None) -> bool:
    return any([EndpointYamlFields.COMPUTE in param for param in params_override])


def load_from_dict(schema: Any, data: Dict, context: Dict, additional_message: str = "", **kwargs):
    try:
        return schema(context=context).load(data, **kwargs)
    except ValidationError as e:
        pretty_error = json.dumps(e.normalized_messages(), indent=2)
        raise ValidationError(decorate_validation_error(schema, pretty_error, additional_message))


def decorate_validation_error(schema: Any, pretty_error: str, additional_message: str = "") -> str:
    ref_doc_link_error_msg = REF_DOC_ERROR_MESSAGE_MAP.get(schema, "")
    if ref_doc_link_error_msg:
        additional_message += f"\n{ref_doc_link_error_msg}"
    additional_message += """\nThe easiest way to author a specification file is using IntelliSense and auto-completion Azure ML VS code extension provides: https://code.visualstudio.com/docs/datascience/azure-machine-learning
To set up: https://docs.microsoft.com/azure/machine-learning/how-to-setup-vs-code"""
    return f"Validation for {schema.__name__} failed:\n\n {pretty_error} \n\n {additional_message}"


def get_md5_string(text):
    try:
        return hashlib.md5(text.encode("utf8")).hexdigest()
    except Exception as ex:
        raise ex


def validate_attribute_type(attrs_to_check: dict, attr_type_map: dict):
    """Validate if attributes of object are set with valid types, raise error
    if don't.

    :param attrs_to_check: Mapping from attributes name to actual value.
    :param attr_type_map: Mapping from attributes name to tuple of expecting type
    """
    #
    kwargs = attrs_to_check.get("kwargs", {})
    attrs_to_check.update(kwargs)
    for attr, expecting_type in attr_type_map.items():
        attr_val = attrs_to_check.get(attr, None)
        if attr_val is not None and not isinstance(attr_val, expecting_type):
            msg = "Expecting {} for {}, got {} instead."
            raise ValidationException(
                message=msg.format(expecting_type, attr, type(attr_val)),
                no_personal_data_message=msg.format(expecting_type, "[attr]", type(attr_val)),
                target=ErrorTarget.GENERAL,
                error_type=ValidationErrorType.INVALID_VALUE,
            )


class SnakeToPascalDescriptor(object):

    """A data descriptor that transforms value from snake_case to CamelCase in
    setter, CamelCase to snake_case in getter.

    When the optional private_name is provided, the descriptor will set
    the private_name in the object's __dict__.
    """

    def __init__(
        self,
        private_name=None,
        *,
        transformer=camel_to_snake,
        reverse_transformer=snake_to_pascal,
    ):
        self.private_name = private_name
        self.transformer = transformer
        self.reverse_transformer = reverse_transformer

    def __set_name__(self, owner, name):
        self.public_name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        key = self.private_name or self.public_name
        value = obj.__dict__.get(key, None)
        return self.transformer(value) if value else None

    def __set__(self, obj, val):

        key = self.private_name or self.public_name
        value = self.reverse_transformer(val)
        obj.__dict__[key] = value

    def __delete__(self, obj):
        key = self.private_name or self.public_name
        obj.__dict__.pop(key, None)


class LiteralToListDescriptor(object):

    """A data descriptor that transforms singular literal values to lists in
    the setter.

    The getter always returns a list When the optional private_name is
    provided, the descriptor will set the private_name in the object's
    __dict__.
    """

    def __init__(self, private_name=None):
        self.private_name = private_name

    def __set_name__(self, owner, name):
        self.public_name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        key = self.private_name or self.public_name
        return obj.__dict__.get(key, None)

    def __set__(self, obj, val):

        key = self.private_name or self.public_name
        if not isinstance(val, list) and val is not None:
            val = [val]
        obj.__dict__[key] = val

    def __delete__(self, obj):
        key = self.private_name or self.public_name
        obj.__dict__.pop(key, None)


def convert_ordered_dict_to_dict(target_object: Union[Dict, List]) -> Union[Dict, List]:
    """Convert ordered dict to dict.

    This is a workaround for rest request must be in dict instead of
    ordered dict.
    """
    # OrderedDict can appear nested in a list
    if isinstance(target_object, list):
        target_object = [convert_ordered_dict_to_dict(obj) for obj in target_object]
    if isinstance(target_object, dict):
        for key, dict_candidate in target_object.items():
            target_object[key] = convert_ordered_dict_to_dict(dict_candidate)
    if isinstance(target_object, OrderedDict):
        return dict(**target_object)
    else:
        return target_object


def _general_copy(src, dst):
    """Wrapped `shutil.copy2` function for possible "Function not implemented"
    exception raised by it.

    Background: `shutil.copy2` will throw OSError when dealing with Azure File.
    See https://stackoverflow.com/questions/51616058 for more information.
    """
    if hasattr(os, "listxattr"):
        with mock.patch("shutil._copyxattr", return_value=[]):
            shutil.copy2(src, dst)
    else:
        shutil.copy2(src, dst)


def get_rest_dict(target_obj, clear_empty_value=False):
    """Convert object to dict and convert OrderedDict to dict."""
    if target_obj is None:
        return None
    result = convert_ordered_dict_to_dict(copy.deepcopy(target_obj.__dict__))
    to_del = ["additional_properties"]
    if clear_empty_value:
        to_del.extend(filter(lambda x: result.get(x) is None, result.keys()))
    for key in to_del:
        if key in result:
            del result[key]
    return result


def extract_label(input_str: str):
    if "@" in input_str:
        return input_str.rsplit("@", 1)
    else:
        return input_str, None


def resolve_pipeline_parameters(pipeline_parameters: dict, remove_empty=False):
    """Resolve pipeline parameters.

    1. Resolve BaseNode and OutputsAttrDict type to PipelineOutputBase.
    2. Remove empty value (optional).
    """

    if pipeline_parameters is None:
        return
    if not isinstance(pipeline_parameters, dict):
        raise ValidationException(
            message="pipeline_parameters must in dict {parameter: value} format.",
            no_personal_data_message="pipeline_parameters must in dict {parameter: value} format.",
            target=ErrorTarget.PIPELINE,
        )

    updated_parameters = {}
    for k, v in pipeline_parameters.items():
        v = resolve_pipeline_parameter(v)
        if v is None and remove_empty:
            continue
        updated_parameters[k] = v
    pipeline_parameters = updated_parameters
    return pipeline_parameters


def resolve_pipeline_parameter(data):
    from azure.ai.ml.entities._builders.base_node import BaseNode
    from azure.ai.ml.entities._builders.pipeline import Pipeline
    from azure.ai.ml.entities._job.pipeline._io import OutputsAttrDict

    if isinstance(data, (BaseNode, Pipeline)):
        # For the case use a node/pipeline node as the input, we use its only one output as the real input.
        # Here we set node = node.outputs, then the following logic will get the output object.
        data = data.outputs
    if isinstance(data, OutputsAttrDict):
        # For the case that use the outputs of another component as the input,
        # we use the only one output as the real input,
        # if multiple outputs are provided, an exception is raised.
        output_len = len(data)
        if output_len != 1:
            raise ValidationException(
                message="Setting input failed: Exactly 1 output is required, got %d. (%s)" % (output_len, data),
                no_personal_data_message="multiple output(s) found of specified outputs, exactly 1 output required.",
                target=ErrorTarget.PIPELINE,
            )
        data = list(data.values())[0]
    return data
