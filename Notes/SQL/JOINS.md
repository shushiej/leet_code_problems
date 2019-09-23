### JOINS

SQL uses JOINS to relate information from multiple tables. 

**Example**:

```
SELECT teams.conference AS conference,
       AVG(players.weight) AS average_weight
  FROM benn.college_football_players players
  JOIN benn.college_football_teams teams
    ON teams.school_name = players.school_name
 GROUP BY teams.conference
 ORDER BY AVG(players.weight) DESC
```

```
SELECT *
  FROM benn.college_football_players players
  JOIN benn.college_football_teams teams
    ON teams.school_name = players.school_name
```
SQL Returns columns from both tables when you include the \*, if you just wanted the columns from the players table you would add **players.**

Refer to this [Viz](https://joins.spathon.com/) on Joins

**INNER JOIN**
![inner_join](https://www.w3schools.com/sql/img_innerjoin.gif)

By default SQL's `JOIN` does an `INNER JOIN`



