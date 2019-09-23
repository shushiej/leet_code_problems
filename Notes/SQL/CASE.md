### CASE

`CASE` allows you to handle IF/THEN logic. THE `CASE` statement is followed by at least one pair of `WHEN` and `THEN` statements. 

`CASE` statements **ALWAYS** appear in the `SELECT` clause. 

```
SELECT player_name,
       year,
       CASE WHEN year = 'SR' THEN 'yes'
            ELSE 'no' END AS is_a_senior
  FROM benn.college_football_players
```

You can also have multiple `WHEN/THEN` clauses.

```
SELECT player_name,
       weight,
       CASE WHEN weight > 250 THEN 'over 250'
            WHEN weight > 200 THEN '201-250'
            WHEN weight > 175 THEN '176-200'
            ELSE '175 or under' END AS weight_group
  FROM benn.college_football_players
```

In the example above the `WHEN/THEN` statements will get evaluated in the order that they're written. So if the `weight` is 300, then it will check the first  statement and then get evaluated. 

**Avoid writing `WHEN/THEN` statements that overlap as above**

You can also string together multiple conditional statements with `AND` and `OR` just as the `WHERE` clause does. 

```
SELECT player_name,
       CASE WHEN year = 'FR' AND position = 'WR' THEN 'frosh_wr'
            ELSE NULL END AS sample_case_statement
  FROM benn.college_football_players
``` 
`CASE` statements can be paired with **aggregate functions**. In cases you wanted to count rows that fulfill a certain condition for example. 

```
SELECT CASE WHEN year = 'FR' THEN 'FR'
            ELSE 'Not FR' END AS year_group,
            COUNT(1) AS count
  FROM benn.college_football_players
 GROUP BY count
```
**Question**
Write a query that counts the number of 300lb+ players for each of the following regions: West Coast (CA, OR, WA), Texas, and Other (Everywhere else).

```
SELECT
    CASE WHEN state in ('CA', 'OR', 'WA') THEN 'West Coast'
          WHEN state = 'TX' THEN 'Texas'
          ELSE 'Other' END AS big_dudes,
          COUNT(1) AS players
    FROM benn.college_football_players
    WHERE weight >= 300
    GROUP BY 1
```

Using Aggregate functions to re-orient the table from Vertical to Horizontal. 

**VERTICAL**
```
SELECT CASE WHEN year = 'FR' THEN 'FR'
            WHEN year = 'SO' THEN 'SO'
            WHEN year = 'JR' THEN 'JR'
            WHEN year = 'SR' THEN 'SR'
            ELSE 'No Year Data' END AS year_group,
            COUNT(1) AS count
  FROM benn.college_football_players
 GROUP BY 1
 ```

 TO **HORIZONTAL**
 ```
SELECT COUNT(CASE WHEN year = 'FR' THEN 1 ELSE NULL END) AS fr_count,
       COUNT(CASE WHEN year = 'SO' THEN 1 ELSE NULL END) AS so_count,
       COUNT(CASE WHEN year = 'JR' THEN 1 ELSE NULL END) AS jr_count,
       COUNT(CASE WHEN year = 'SR' THEN 1 ELSE NULL END) AS sr_count
  FROM benn.college_football_players
 ```