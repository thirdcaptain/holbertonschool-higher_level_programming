-- create a table unique_id with unique id of default value 1
CREATE TABLE IF NOT EXISTS unique_id (
       id    	INT 	     DEFAULT 1    UNIQUE,
       name	VARCHAR(256)
);
