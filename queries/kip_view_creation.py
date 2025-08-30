from shared.constants import GCP_DATASET, GCP_PROJECT, GCP_TABLE, GCP_KIP_VIEW

KIP_VIEW_CREATION = f"""
CREATE VIEW {GCP_PROJECT}.{GCP_DATASET}.{GCP_KIP_VIEW} AS (
    SELECT
        date,
        ROUND(SUM(spend / conversions), 2) as cac,
        ROUND(SUM((conversions * 100) / spend), 2) as roas
    FROM `{GCP_PROJECT}.{GCP_DATASET}.{GCP_TABLE}`
    GROUP BY date
);
"""
