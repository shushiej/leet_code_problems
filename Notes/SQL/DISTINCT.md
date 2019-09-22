### DISTINCT

Selects all the unique values in the table.
Having two or more columns in the `DISTINCT` clause will give you unique pairs of each column.

```
SELECT DISTINCT year, month
  FROM tutorial.aapl_historical_stock_price
```

`DISTINCT` can be useful when exploring a new dataset. Looking at unique values can help you figure out how you may want to group or filter the data.

#### Using DISTINCT with aggregations
You can use `DISTINCT` when performing aggregations most commonly `COUNT` to get the number of unique values in the column. 

```
SELECT
     year,
     COUNT(DISTINCT month) AS "Unique Months"
    FROM tutorial.aapl_historical_stock_price
    GROUP BY year
    ORDER BY year
```

#### DISTINCT Performance
Using `DISTINCT` in aggregations can slow your queries down quite a bit. 