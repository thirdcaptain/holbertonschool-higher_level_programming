-- create a database hbtn_0d_usa and table cities
-- cities table has enumerated primary key id
-- cities table has foreign key that references id of states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id    	    INT 	 NOT NULL   UNIQUE  AUTO_INCREMENT,
       state_id    INT		 NOT NULL,
       name	    VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id)
);
