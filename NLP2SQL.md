How does “Compare CAC and ROAS for last 30 days vs prior 30 days.” translate to SQL?
- `Compare` => Intent: have both values in the result. No grouping needed.
- `for last 30 days` => First where condition. Also denotes aggregation for the given period. `WHERE date BETWEEN CURRENT_DATE() - INTERVAL 30 DAY AND CURRENT_DATE()`
- `vs prior 30 days` => Second where condition. Denotes aggregation as well. `WHERE date BETWEEN CURRENT_DATE() - INTERVAL 60 DAY AND CURRENT_DATE() - INTERVAL 31 DAY`
- `CAC and ROAS` => The columns to select. `SELECT SUM(CAC), SUM(ROAS)` 
- `last 30 days` and `prior 30 days` => We need to differentiate the two periods in the result. This can be done with CTEs for better readability.
- As we have 2 CTEs, we can use a `CROSS JOIN` to combine the results into one row.

