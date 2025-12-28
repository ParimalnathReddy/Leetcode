CREATE TABLE Friendship (
    user1_id INT,
    user2_id INT
);
INSERT INTO Friendship (user1_id, user2_id) VALUES
(1, 2),
(1, 3),
(1, 4),
(2, 3),
(2, 4),
(2, 5),
(6, 1);


CREATE TABLE Likes (
    user_id INT,
    page_id INT
);


INSERT INTO Likes (user_id, page_id) VALUES
(1, 88),
(2, 23),
(3, 24),
(4, 56),
(5, 11),
(6, 33),
(2, 77),
(3, 77),
(6, 88);


with cte as 

(SELECT CASE when user1_id = 1 then user2_id 
When user2_id = 1 then user1_id end as friends

FROM Friendship)


SELECT DISTINCT page_id as recommended_page
FROM likes
where user_id IN (SELECT friends from cte )
AND page_id NOT IN (select page_id from Likes 
WHERE user_id = 1 )