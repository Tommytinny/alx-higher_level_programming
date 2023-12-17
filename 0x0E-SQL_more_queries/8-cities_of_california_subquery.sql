--  lists all the cities of California that can be found in the database

SELECT * FROM cities WHERE state_id IN (SELECT id FROM states WHERE name="California") ORDER BY id ASC;
