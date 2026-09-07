from dataclasses import dataclass
from typing import Literal
import datetime


@dataclass
class bankAccount:
    institution: str
    type: Literal["checking", "savings"]
    owner: str
    value: float
    interest_percent: float
    last_updated: datetime


@dataclass
class investmentAccount:
    institution: str
    type: Literal[
        "IRA",
        "401k",
        "403b",
        "HSA",
        "Brokerage",
    ]
    tax_advantage: Literal["Traditional", "Roth", "Triple", "None"]
    owner: str
    value: float
    principal: float
    last_updated: datetime
