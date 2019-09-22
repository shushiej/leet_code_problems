### Having

The `HAVING` clause allows you to perform conditional requests on Aggregated Functions, unlike the `WHERE` clause which does not allow conditional requests on **aggregate** functions. 

eg.

```
SELECT year,
       month,
       MAX(high) AS month_high
    FROM tutorial.aapl_historical_stock_price
    GROUP BY year, month
    HAVING MAX(high) > 400
    ORDER BY year, month
```

`HAVING` is a clean way to filter a query that has been aggregated, but this is also commonly done using `subquery`.

The Order which you write clauses is important:

1. `SELECT`
2. `FROM`
3. `WHERE`
4. `GROUP BY`
5. `HAVING`
6. `ORDER BY`