-- Create the table
CREATE TABLE tasks (
    task_id INT,
    assignee_id INT,
    submit_date DATE
);

-- Insert the records
INSERT INTO tasks (task_id, assignee_id, submit_date) VALUES
(1, 1, '2022-06-13'),
(2, 6, '2022-06-14'),
(3, 6, '2022-06-15'),
(4, 3, '2022-06-18'),
(5, 5, '2022-06-19'),
(6, 7, '2022-06-19');



SELECT SUM(CASE WHEN DAYOFWEEK(submit_date) IN (1,7) THEN 1 ELSE 0 END) AS weekend_cnt, 
         SUM(CASE WHEN DAYOFWEEK(submit_date) NOT IN (1,7) THEN 1 ELSE 0 END) AS weekday_cnt
FROM tasks;