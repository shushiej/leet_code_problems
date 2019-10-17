-- write your code in PostgreSQL 9.4
SELECT 
    t.team_id,
    t.team_name,
    SUM(CASE 
        WHEN t.team_id = m.host_team THEN
            CASE
                WHEN m.host_goals > m.guest_goals THEN 3
                WHEN m.host_goals = m.guest_goals THEN 1
                ELSE 0
                END
        ELSE
            CASE
                WHEN m.host_goals < m.guest_goals THEN 3
                WHEN m.host_goals = m.guest_goals THEN 1
                ELSE 0
            END
        END) AS num_points
FROM 
    matches m
RIGHT JOIN teams t
    ON t.team_id in (m.host_team, m.guest_team)
GROUP BY
    t.team_name,
    t.team_id
ORDER BY 
    num_points DESC