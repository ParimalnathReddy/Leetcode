CREATE TABLE rides (
    ride_id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT
);

INSERT INTO rides (ride_id, driver_id, passenger_id)
VALUES
    (1, 7, 1),
    (2, 7, 2),
    (3, 11, 1),
    (4, 11, 7),
    (5, 11, 7),
    (6, 11, 3);

WITH CTE As
(SELECT passenger_id, COUNT(*) as num_of_rides
FROM Rides 
GROUP BY passenger_id)

select DISTINCT r.driver_id, CASE WHEN c.num_of_rides IS NOT NULL THEN C.num_of_rides 
ELSE 0 END AS cnt
FROM Rides R
LEFT JOIN CTE C ON r.driver_id = c.passenger_id