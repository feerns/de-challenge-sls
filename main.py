import datetime

from fastapi import FastAPI

from bq_connector.bq_client import get_bq_client
from queries.analysis_query import ANALYSIS_QUERY
from shared.constants import GCP_PROJECT
from shared.models import DateRange, AnalyticsResult

app = FastAPI()
BQ_CLIENT = get_bq_client(GCP_PROJECT)


@app.get("/")
async def root():
    return {"Welcome": "to the results of the Challenge!"}


@app.get("/metrics/", response_model=list[AnalyticsResult])
async def get_metrics(start_date: str = '2025-01-01', end_date: str = '2025-01-31') -> list[AnalyticsResult]:
    date_range = DateRange(start_date=start_date, end_date=end_date)
    query = ANALYSIS_QUERY.format(
        start_date=date_range.start_date,
        end_date=date_range.end_date,
    )
    results = BQ_CLIENT.query(query).result()
    return [AnalyticsResult(**dict(row)) for row in results]
