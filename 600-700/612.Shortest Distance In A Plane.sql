SELECT p1.x AS 'p1.x', p1.y AS 'p1.y', p2.x AS 'p2.x', p2.y AS 'p2.y' , SQRT(POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)) AS 'distance' 
FROM point_2d p1, 
INNER JOIN point_2d p2 ON p1.x != p2.x OR p1.y != p2.y;