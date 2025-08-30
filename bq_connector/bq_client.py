
from google.cloud import bigquery

def get_bq_client(project_id: str) -> bigquery.Client:
    return bigquery.Client(project_id)
