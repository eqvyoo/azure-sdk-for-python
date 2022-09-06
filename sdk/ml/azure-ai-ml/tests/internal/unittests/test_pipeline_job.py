# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
from pathlib import Path

import pydash
import pytest
import yaml
from tests.internal._utils import (
    DATA_VERSION,
    PARAMETERS_TO_TEST,
    assert_strong_type_intellisense_enabled,
    extract_non_primitive,
    set_run_settings,
)

from azure.ai.ml import Input, load_component
from azure.ai.ml._internal.entities.component import InternalComponent
from azure.ai.ml._internal.entities.node import InternalBaseNode
from azure.ai.ml._internal.entities.scope import Scope
from azure.ai.ml.constants._common import AssetTypes, InputOutputModes
from azure.ai.ml.dsl import pipeline
from azure.ai.ml.entities import CommandComponent, Data, PipelineJob


@pytest.mark.usefixtures("enable_internal_components")
@pytest.mark.unittest
class TestPipelineJob:
    @pytest.mark.parametrize(
        "yaml_path,inputs,runsettings_dict,pipeline_runsettings_dict",
        PARAMETERS_TO_TEST,
    )
    def test_anonymous_internal_component_in_pipeline(
        self, yaml_path, inputs, runsettings_dict, pipeline_runsettings_dict
    ):
        node_func: InternalComponent = load_component(yaml_path)

        @pipeline()
        def pipeline_func():
            node = node_func(**inputs)
            set_run_settings(node, runsettings_dict)
            assert_strong_type_intellisense_enabled(node, runsettings_dict)

        dsl_pipeline: PipelineJob = pipeline_func()
        set_run_settings(dsl_pipeline.settings, pipeline_runsettings_dict)
        result = dsl_pipeline._validate()
        assert result._to_dict() == {"result": "Succeeded"}

        node_rest_dict = dsl_pipeline._to_rest_object().properties.jobs["node"]
        del node_rest_dict["componentId"]  # delete component spec to make it a pure dict
        mismatched_runsettings = {}
        dot_key_map = {"compute": "computeId"}
        for dot_key, expected_value in runsettings_dict.items():
            if dot_key in dot_key_map:
                dot_key = dot_key_map[dot_key]

            # hack: timeout will be transformed into str
            if dot_key == "limits.timeout":
                expected_value = "PT5M"
            value = pydash.get(node_rest_dict, dot_key)
            if value != expected_value:
                mismatched_runsettings[dot_key] = (value, expected_value)
        assert not mismatched_runsettings, "Current value:\n{}\nMismatched fields:\n{}".format(
            json.dumps(node_rest_dict, indent=2), json.dumps(mismatched_runsettings, indent=2)
        )

        pipeline_dict = dsl_pipeline._to_dict()
        pipeline_dict = extract_non_primitive(pipeline_dict)
        assert not pipeline_dict, pipeline_dict

    @pytest.mark.parametrize(
        "yaml_path,inputs,runsettings_dict,pipeline_runsettings_dict",
        PARAMETERS_TO_TEST,
    )
    def test_data_as_pipeline_inputs(self, yaml_path, inputs, runsettings_dict, pipeline_runsettings_dict):
        node_func: InternalComponent = load_component(yaml_path)

        input_data_names = {}
        for input_name, input_obj in inputs.items():
            if isinstance(input_obj, Input):
                data_name = input_obj.path.split("@")[0]
                inputs[input_name] = Data(name=data_name, version=DATA_VERSION, type=AssetTypes.MLTABLE)
                input_data_names[input_name] = data_name
        if len(input_data_names) == 0:
            return

        @pipeline()
        def pipeline_func():
            node = node_func(**inputs)
            set_run_settings(node, runsettings_dict)
            assert_strong_type_intellisense_enabled(node, runsettings_dict)

        dsl_pipeline: PipelineJob = pipeline_func()
        set_run_settings(dsl_pipeline.settings, pipeline_runsettings_dict)
        result = dsl_pipeline._validate()
        assert result._to_dict() == {"result": "Succeeded"}

        node_rest_dict = dsl_pipeline._to_rest_object().properties.jobs["node"]
        for input_name, dataset_name in input_data_names.items():
            expected_rest_obj = {
                "job_input_type": AssetTypes.MLTABLE,
                "uri": dataset_name + ":" + DATA_VERSION,
            }
            assert node_rest_dict["inputs"][input_name] == expected_rest_obj

    def test_ipp_internal_component_in_pipeline(self):
        yaml_path = "./tests/test_configs/internal/ipp-component/spec.yaml"
        # TODO: support anonymous ipp component creation
        # curated env with name & version
        # command_func: InternalComponent = client.components.get("ls_command", "0.0.1")
        node_func: InternalComponent = load_component(yaml_path)

        @pipeline()
        def pipeline_func():
            node_func()

        dsl_pipeline: PipelineJob = pipeline_func()
        result = dsl_pipeline._validate()
        assert result._to_dict() == {"result": "Succeeded"}

    @pytest.mark.skip(reason="not implemented")
    def test_gjd_internal_component_in_pipeline(self):
        yaml_path = "./tests/test_configs/internal/ls_command_component.yaml"  # GJD is based on CommandComponent
        node_func: CommandComponent = load_component(yaml_path)
        node_func()

    @pytest.mark.skip(reason="not implemented")
    def test_elastic_component_in_pipeline(self):
        yaml_path = (
            "./tests/test_configs/internal/ls_command_component.yaml"  # itp & elastic are based on CommandComponent
        )
        node_func: CommandComponent = load_component(yaml_path)
        node_func()

    @pytest.mark.skip(reason="not implemented")
    def test_singularity_component_in_pipeline(self):
        yaml_path = (
            "./tests/test_configs/internal/ls_command_component.yaml"  # singularity is based on CommandComponent
        )
        node_func: CommandComponent = load_component(yaml_path)
        node_func()

    def test_load_pipeline_job_with_internal_components_as_node(self):
        yaml_path = Path("./tests/test_configs/internal/helloworld_component_scope.yml")
        scope_internal_func = load_component(source=yaml_path)
        with open(yaml_path, encoding="utf-8") as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
        command_func = load_component("./tests/test_configs/components/helloworld_component.yml")

        @pipeline()
        def pipeline_func():
            node = command_func(component_in_path=Input(path="./tests/test_configs/data"))
            node.compute = "cpu-cluster"

            node_internal: Scope = scope_internal_func(
                TextData=Input(type=AssetTypes.MLTABLE, path="azureml:scope_tsv:1"),
                ExtractionClause="column1:string, column2:int",
            )

            node_internal.priority = 800
            node_internal.adla_account_name = "adla_account_name"
            node_internal.scope_param = "-tokens 50"
            node_internal.custom_job_name_suffix = "component_sdk_test"

        dsl_pipeline: PipelineJob = pipeline_func()
        internal_node_name = "node_internal"
        assert dsl_pipeline.jobs[internal_node_name]._component._to_dict() == yaml_dict

        scope_node: InternalBaseNode = dsl_pipeline.jobs[internal_node_name]
        # TODO: check why need to set base path manually
        scope_node._set_base_path(yaml_path.parent)
        scope_node_dict = scope_node._to_dict()
        assert scope_node_dict == {
            "$schema": "{}",
            "priority": 800,
            "adla_account_name": "adla_account_name",
            "custom_job_name_suffix": "component_sdk_test",
            "scope_param": "-tokens 50",
            "component": yaml_dict,
            "type": "ScopeComponent",
            "inputs": {
                "ExtractionClause": "column1:string, column2:int",
                "TextData": {"path": "azureml:scope_tsv:1", "type": "mltable"},
            },
            "outputs": {},
        }
        assert pydash.omit(scope_node._to_rest_object(), "componentId") == {
            "_source": "YAML.COMPONENT",
            "priority": 800,
            "adla_account_name": "adla_account_name",
            "custom_job_name_suffix": "component_sdk_test",
            "scope_param": "-tokens 50",
            "inputs": {
                "ExtractionClause": {"job_input_type": "literal", "value": "column1:string, column2:int"},
                "TextData": {"job_input_type": "mltable", "uri": "azureml:scope_tsv:1"},
            },
            "outputs": {},
            "type": "ScopeComponent",
        }
        scope_node._validate(raise_error=True)

        omit_fields = ["jobs.node.component", "jobs.node_internal.component"]
        assert pydash.omit(dsl_pipeline._to_dict(), *omit_fields) == pydash.omit(
            {
                "display_name": "pipeline_func",
                "inputs": {},
                "jobs": {"node": dsl_pipeline.jobs["node"]._to_dict(), "node_internal": scope_node._to_dict()},
                "outputs": {},
                "properties": {},
                "settings": {},
                "tags": {},
                "type": "pipeline",
            },
            *omit_fields,
        )

        dsl_pipeline._validate(raise_error=True)

        rest_object = dsl_pipeline._to_rest_object()
        assert rest_object.properties.jobs == {
            "node": dsl_pipeline.jobs["node"]._to_rest_object(),
            "node_internal": scope_node._to_rest_object(),
        }
