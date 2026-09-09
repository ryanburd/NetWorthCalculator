from dataclasses import dataclass
from typing import Literal
import datetime


@dataclass
class studentLoans:
    institution: str
    owner: str
    monthly_value: float
    yearly_value: float
    remaining_total: float
    months_remaining: int
    last_updated: datetime


@dataclass
class carLoan:
    institution: str
    owner: str
    monthly_value: float
    yearly_value: float
    remaining_total: float
    months_remaining: int
    last_updated: datetime
