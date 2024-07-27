
WITH cte AS
(SELECT *, DENSE_RANK() OVER (PARTITION BY city_id ORDER BY degree DECS ,day) as rank
FROM Weather)

SELECT city_id, day, degree
FROM cte
WHERE rank = 1
ORDER BY city_id
-- hello