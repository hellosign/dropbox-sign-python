# coding: utf-8

"""
    Dropbox Sign API

    Dropbox Sign v3 API

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FaxLineAreaCodeGetProvinceEnum(str, Enum):
    """
    FaxLineAreaCodeGetProvinceEnum
    """

    """
    allowed enum values
    """
    AB = 'AB'
    BC = 'BC'
    MB = 'MB'
    NB = 'NB'
    NL = 'NL'
    NT = 'NT'
    NS = 'NS'
    NU = 'NU'
    ON = 'ON'
    PE = 'PE'
    QC = 'QC'
    SK = 'SK'
    YT = 'YT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FaxLineAreaCodeGetProvinceEnum from a JSON string"""
        return cls(json.loads(json_str))


