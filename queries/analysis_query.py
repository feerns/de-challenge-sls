from shared.constants import GCP_PROJECT, GCP_DATASET, GCP_KIP_VIEW

ANALYSIS_QUERY = f"""
DECLARE start_date, end_date, second_start_date, second_end_date DATE;

SET start_date = '{{start_date}}';
SET end_date = '{{end_date}}';
SET second_start_date = DATE_SUB(start_date, INTERVAL 31 DAY);
SET second_end_date = DATE_SUB(start_date, INTERVAL 1 DAY);


WITH thirty_days AS (
  SELECT
    SUM(cac) AS total_cac,
    SUM(roas) AS total_roas
  FROM `{GCP_PROJECT}.{GCP_DATASET}.{GCP_KIP_VIEW}`
  WHERE date BETWEEN start_date AND end_date
), previous_thirty_days AS (
  SELECT
    SUM(cac) AS total_cac,
    SUM(roas) AS total_roas
  FROM `{GCP_PROJECT}.{GCP_DATASET}.{GCP_KIP_VIEW}`
  WHERE date BETWEEN second_start_date AND second_end_date
), absolute_values AS (
  SELECT
    td.total_cac as thirty_days_cac,
    td.total_roas as thirty_days_roas,
    -- std.total_cac as second_thirty_days_cac,
    -- std.total_roas as second_thirty_days_roas,
    (
      SELECT total_cac FROM previous_thirty_days
    ) as previous_thirty_days_cac,
    (
      SELECT total_roas FROM previous_thirty_days
    ) as previous_thirty_days_roas,
  FROM thirty_days td
  -- CROSS JOIN second_thirty_days as std
)
SELECT
  start_date AS thirty_days_start,
  end_date AS thirty_days_end,
  second_start_date AS previous_thirty_days_start,
  second_end_date AS previous_thirty_days_end,
  *,
  (COALESCE(previous_thirty_days_cac, 0) - COALESCE(thirty_days_cac, 0)) / COALESCE(previous_thirty_days_cac, thirty_days_cac) AS percentage_difference_cac,
  (COALESCE(previous_thirty_days_roas, 0) - COALESCE(thirty_days_roas, 0)) / COALESCE(previous_thirty_days_roas, thirty_days_roas) AS percentage_difference_roas
FROM absolute_values

"""