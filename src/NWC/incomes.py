from dataclasses import dataclass
from typing import Literal
import datetime


@dataclass
class salary:
    institution: str
    owner: str
    monthly_value: float
    yearly_value: float
    last_updated: datetime


@dataclass
class inheritance:
    institution: str
    owner: str
    monthly_value: float
    yearly_value: float
    last_updated: datetime
