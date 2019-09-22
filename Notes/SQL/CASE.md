### CASE

`CASE` allows you to handle IF/THEN logic. THE `CASE` statement is followed by at least one pair of `WHEN` and `THEN` statements. 

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