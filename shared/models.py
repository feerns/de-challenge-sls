
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class DateRange(BaseModel):
    start_date: date= Field(default='2025-01-01', description="Start date in YYYY-MM-DD format")
    end_date: date = Field(default='2025-01-31', description="Start date in YYYY-MM-DD format")


class AnalyticsResult(BaseModel):
    thirty_days_start: date
    thirty_days_end: date
    previous_thirty_days_start: date
    previous_thirty_days_end: date
    thirty_days_cac: Optional[float] = Field( default=0)
    thirty_days_roas: Optional[float] = Field(default=0)
    previous_thirty_days_cac: Optional[float] = Field(default=0)
    previous_thirty_days_roas: Optional[float] = Field(default=0)
    percentage_difference_cac: Optional[float]
    percentage_difference_roas: Optional[float]