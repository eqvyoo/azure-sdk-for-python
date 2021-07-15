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

from enum import Enum


class BillingFrequency(str, Enum):

    month = "Month"
    quarter = "Quarter"
    year = "Year"


class CategoryType(str, Enum):

    cost = "Cost"
    usage = "Usage"


class TimeGrainType(str, Enum):

    monthly = "Monthly"
    quarterly = "Quarterly"
    annually = "Annually"


class OperatorType(str, Enum):

    equal_to = "EqualTo"
    greater_than = "GreaterThan"
    greater_than_or_equal_to = "GreaterThanOrEqualTo"


class Grain(str, Enum):

    daily = "Daily"
    monthly = "Monthly"
    yearly = "Yearly"


class ChargeType(str, Enum):

    actual = "Actual"
    forecast = "Forecast"


class Bound(str, Enum):

    upper = "Upper"
    lower = "Lower"


class Datagrain(str, Enum):

    daily_grain = "daily"  #: Daily grain of data
    monthly_grain = "monthly"  #: Monthly grain of data


class Metrictype(str, Enum):

    actual_cost_metric_type = "actualcost"  #: Actual cost data.
    amortized_cost_metric_type = "amortizedcost"  #: Amortized cost data.
    usage_metric_type = "usage"  #: Usage data.