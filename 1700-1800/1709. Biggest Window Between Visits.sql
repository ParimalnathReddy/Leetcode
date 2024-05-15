
WITH CTE AS (
    SELECT *, LEAD(visit_date,1) OVER(PARTITION BY user_id ORDER BY visit_date) as next_visit_date
    FROM UserVisits
)

CTE2 AS
(SELECT user_id, case when next_visit_date is NOT NULL THEN DATEDIFF(next_visit_date , visit_date) ELSE DATEDIFF(CAST('2021-01-01' AS DATE ),visit_date) as windw
FROM CTE)

SELECT user_id, MAX(windw) as biggest_window
FROM CTE2
GROUP BY user_id