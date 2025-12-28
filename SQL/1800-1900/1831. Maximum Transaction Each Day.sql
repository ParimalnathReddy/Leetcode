CREATE TABLE Transactions (
    transaction_id INT,
    day DATETIME,
    amount INT
);

INSERT INTO Transactions (transaction_id, day, amount) VALUES
(8, '2021-04-03 15:57:28', 57),
(9, '2021-04-28 08:47:25', 21),
(1, '2021-04-29 13:28:30', 58),
(5, '2021-04-28 16:39:59', 40),
(6, '2021-04-29 23:39:28', 58);

WITH cte AS 
(SELECT transaction_id,DATE_FORMAT(day,'%Y-%m-%d') AS Day, amount 
FROM Transactions),

cte2 AS
(SELECT *, FIRST_VALUE(amount) OVER (PARTITION BY day ORDER BY amount DESC ) AS maximum_amount
FROM cte)

SELECT transaction_id
FROM cte1
WHERE amount = maximum_amount
ORDER BY transaction_id