-- list all score,name of all records in second_table table, skipping rows without name
SELECT score, name
FROM second_table
WHERE name != 'NULL'
ORDER BY score DESC;
