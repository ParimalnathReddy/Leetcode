CREATE TABLE friends (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    activity_id INT,
    FOREIGN KEY (activity_id) REFERENCES activities(id)
);

CREATE TABLE activities (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO activities (id, name)
VALUES
    (1, 'Eating'),
    (2, 'Singing'),
    (3, 'Horse Riding');

INSERT INTO friends (id, name, activity_id)
VALUES
    (1, 'Jonathan D.', 1),
    (2, 'Jade W.', 2),
    (3, 'Victor J.', 2),
    (4, 'Elvis Q.', 1),
    (5, 'Daniel A.', 1),
    (6, 'Bob B.', 3);


WITH CTE AS (
    SELECT activity, COUNT(ID) AS num_part
    FROM Friends 
    GROUP BY activity
)

SELECT a.name, CASE WHEN 
FROM Activities a 
LEFT JOIN cte c 
ON a.name = c.activity
