# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from .._generated.models._microsoft_azure_metrics_advisor_restapi_open_ap_iv2_enums import (
    SnoozeScope,
    Severity as AnomalySeverity,
    DataSourceType as DatasourceType,
    ViewMode as DataFeedAccessMode,
    RollUpMethod as DataFeedAutoRollupMethod,
    FillMissingPointType as DatasourceMissingDataPointFillType,
    AnomalyDetectorDirection,
    IncidentStatus as AnomalyIncidentStatus,
    Granularity as DataFeedGranularityType,
    EntityStatus as DataFeedStatus,
    AnomalyValue,
    ChangePointValue,
    PeriodType,
    FeedbackType,
    TimeMode as AlertQueryTimeMode,
    DataSourceCredentialType as DatasourceCredentialType,
    AuthenticationTypeEnum as DatasourceAuthenticationType
)

from .._generated.models import (
    FeedbackQueryTimeMode,
    RootCause,
    DimensionGroupIdentity,
    DetectionIncidentFilterCondition,
    EnrichmentStatus,
    MetricSeriesItem as MetricSeriesDefinition,
    IngestionStatus as DataFeedIngestionStatus,
    SeriesIdentity,
    SeverityFilterCondition
)

from ._models import (
    MetricFeedback,
    AnomalyFeedback,
    ChangePointFeedback,
    CommentFeedback,
    PeriodFeedback,
    MetricAnomalyAlertConfigurationsOperator,
    DataFeedGranularity,
    DataFeedIngestionSettings,
    DataFeedMissingDataPointFillSettings,
    DataFeedRollupSettings,
    DataFeedSchema,
    DataFeed,
    MetricAnomalyAlertScope,
    MetricAlertConfiguration,
    AzureApplicationInsightsDataFeedSource,
    AzureBlobDataFeedSource,
    AzureCosmosDbDataFeedSource,
    AzureTableDataFeedSource,
    AzureLogAnalyticsDataFeedSource,
    InfluxDbDataFeedSource,
    SqlServerDataFeedSource,
    MongoDbDataFeedSource,
    MySqlDataFeedSource,
    PostgreSqlDataFeedSource,
    AzureDataExplorerDataFeedSource,
    AnomalyAlertConfiguration,
    NotificationHook,
    EmailNotificationHook,
    WebNotificationHook,
    TopNGroupScope,
    SeverityCondition,
    MetricAnomalyAlertSnoozeCondition,
    MetricBoundaryCondition,
    MetricDetectionCondition,
    MetricSeriesGroupDetectionCondition,
    SmartDetectionCondition,
    HardThresholdCondition,
    SuppressCondition,
    ChangeThresholdCondition,
    MetricSingleSeriesDetectionCondition,
    DataFeedDimension,
    DataFeedMetric,
    DataFeedIngestionProgress,
    DetectionConditionOperator,
    AnomalyDetectionConfiguration,
    MetricAnomalyAlertConditions,
    AnomalyIncident,
    DataPointAnomaly,
    MetricSeriesData,
    AnomalyAlert,
    AzureDataLakeStorageGen2DataFeedSource,
    AzureEventHubsDataFeedSource,
    MetricAnomalyAlertScopeType,
    DataFeedRollupType,
    IncidentRootCause,
    MetricEnrichedSeriesData,
    DatasourceSqlConnectionString,
    DatasourceDataLakeGen2SharedKey,
    DatasourceServicePrincipal,
    DatasourceServicePrincipalInKeyVault,
    DatasourceCredential,
    DataFeedSource,
    DetectionAnomalyFilterCondition,
)


__all__ = (
    "MetricFeedback",
    "AnomalyFeedback",
    "ChangePointFeedback",
    "CommentFeedback",
    "PeriodFeedback",
    "FeedbackQueryTimeMode",
    "RootCause",
    "AnomalyAlertConfiguration",
    "DetectionAnomalyFilterCondition",
    "DimensionGroupIdentity",
    "AnomalyIncident",
    "DetectionIncidentFilterCondition",
    "AnomalyDetectionConfiguration",
    "MetricAnomalyAlertConfigurationsOperator",
    "DataFeedStatus",
    "DataFeedGranularity",
    "DataFeedIngestionSettings",
    "DataFeedMissingDataPointFillSettings",
    "DataFeedRollupSettings",
    "DataFeedSchema",
    "DataFeedDimension",
    "DataFeedMetric",
    "DataFeed",
    "TopNGroupScope",
    "MetricAnomalyAlertScope",
    "MetricAlertConfiguration",
    "SnoozeScope",
    "AnomalySeverity",
    "MetricAnomalyAlertSnoozeCondition",
    "MetricBoundaryCondition",
    "AzureApplicationInsightsDataFeedSource",
    "AzureBlobDataFeedSource",
    "AzureCosmosDbDataFeedSource",
    "AzureTableDataFeedSource",
    "AzureLogAnalyticsDataFeedSource",
    "InfluxDbDataFeedSource",
    "SqlServerDataFeedSource",
    "MongoDbDataFeedSource",
    "MySqlDataFeedSource",
    "PostgreSqlDataFeedSource",
    "AzureDataExplorerDataFeedSource",
    "MetricDetectionCondition",
    "MetricSeriesGroupDetectionCondition",
    "MetricSingleSeriesDetectionCondition",
    "SeverityCondition",
    "DatasourceType",
    "MetricAnomalyAlertScopeType",
    "AnomalyDetectorDirection",
    "NotificationHook",
    "EmailNotificationHook",
    "WebNotificationHook",
    "DataFeedIngestionProgress",
    "DetectionConditionOperator",
    "MetricAnomalyAlertConditions",
    "EnrichmentStatus",
    "DataFeedGranularityType",
    "DataPointAnomaly",
    "AnomalyIncidentStatus",
    "MetricSeriesData",
    "MetricSeriesDefinition",
    "AnomalyAlert",
    "DataFeedAccessMode",
    "DataFeedRollupType",
    "DataFeedAutoRollupMethod",
    "DatasourceMissingDataPointFillType",
    "DataFeedIngestionStatus",
    "SmartDetectionCondition",
    "SuppressCondition",
    "ChangeThresholdCondition",
    "HardThresholdCondition",
    "SeriesIdentity",
    "AzureDataLakeStorageGen2DataFeedSource",
    "AzureEventHubsDataFeedSource",
    "AnomalyValue",
    "ChangePointValue",
    "PeriodType",
    "FeedbackType",
    "AlertQueryTimeMode",
    "IncidentRootCause",
    "SeverityFilterCondition",
    "MetricEnrichedSeriesData",
    "DatasourceSqlConnectionString",
    "DatasourceDataLakeGen2SharedKey",
    "DatasourceServicePrincipal",
    "DatasourceServicePrincipalInKeyVault",
    "DatasourceCredentialType",
    "DatasourceAuthenticationType",
    "DatasourceCredential",
    "DataFeedSource",
)
