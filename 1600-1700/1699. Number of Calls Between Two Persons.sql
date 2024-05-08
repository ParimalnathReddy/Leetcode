

SELECT CASE WHEN from_if < to_id THEN from_id ELSE to_id END AS person1,
       CASE WHEN from_id < to_id THEN to_id ELSE from_id END AS person2,
       COUNT(*) AS call_count
FROM calls