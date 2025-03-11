-- lists all the cities of California that can be found in the database `hbtn_0d_usa`
SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California') 
AND name IN ('San Francisco', 'San Diego', 'San Jose') 
ORDER BY id ASC;
