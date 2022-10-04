# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class RuleSeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The rule severity."""

    #: High
    HIGH = "High"
    #: Medium
    MEDIUM = "Medium"
    #: Low
    LOW = "Low"
    #: Informational
    INFORMATIONAL = "Informational"
    #: Obsolete
    OBSOLETE = "Obsolete"


class RuleStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The rule result status."""

    #: NonFinding
    NON_FINDING = "NonFinding"
    #: Finding
    FINDING = "Finding"
    #: InternalError
    INTERNAL_ERROR = "InternalError"


class RuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The rule type."""

    #: Binary
    BINARY = "Binary"
    #: BaselineExpected
    BASELINE_EXPECTED = "BaselineExpected"
    #: PositiveList
    POSITIVE_LIST = "PositiveList"
    #: NegativeList
    NEGATIVE_LIST = "NegativeList"


class ScanState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scan status."""

    #: Failed
    FAILED = "Failed"
    #: FailedToRun
    FAILED_TO_RUN = "FailedToRun"
    #: InProgress
    IN_PROGRESS = "InProgress"
    #: Passed
    PASSED = "Passed"


class ScanTriggerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scan trigger type."""

    #: OnDemand
    ON_DEMAND = "OnDemand"
    #: Recurring
    RECURRING = "Recurring"