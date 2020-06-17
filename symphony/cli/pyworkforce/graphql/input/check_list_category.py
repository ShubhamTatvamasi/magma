#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from functools import partial
from gql.gql.datetime_utils import DATETIME_FIELD
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin

from ..input.check_list_item import CheckListItemInput
@dataclass
class CheckListCategoryInput(DataClassJsonMixin):
    title: str
    checkList: List[CheckListItemInput]
    id: Optional[str] = None
    description: Optional[str] = None
