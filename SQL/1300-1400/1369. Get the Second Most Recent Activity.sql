
CREATE TABLE UserActivity (
    username VARCHAR(50),
    activity VARCHAR(50),
    startDate DATE,
    endDate DATE
);

INSERT INTO UserActivity (username, activity, startDate, endDate) VALUES
('Alice', 'Travel', '2020-02-12', '2020-02-20'),
('Alice', 'Dancing', '2020-02-21', '2020-02-23'),
('Alice', 'Travel', '2020-02-24', '2020-02-28'),
('Bob', 'Travel', '2020-02-11', '2020-02-18');

-- FROM cte
-- (SELECT DISTINCT *
-- FROM UserActivity),

-- cte2 as
-- (SELECT *,ROW_NUMBER() OVER(PARTITION BY username ORDER BY startData DESC) as row_username,
-- COUNT(activity) OVER(PARTITION BY username)  as user_names
-- FROM cte)

-- SELECT * FROM cte2;

WITH cte AS (
    SELECT DISTINCT *
    FROM UserActivity
),
cte2 AS (
    SELECT *,
           ROW_NUMBER() OVER(PARTITION BY username ORDER BY startDate DESC) AS row_username,
           COUNT(activity) OVER(PARTITION BY username) AS user_names
    FROM cte
)
SELECT username, activity,startDate,endDate 
FROM cte2
WHERE row_username = 2 
OR user_names = 1
