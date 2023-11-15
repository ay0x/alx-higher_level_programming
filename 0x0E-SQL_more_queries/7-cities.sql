-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

--Switch to databse
USE hbtn_0d_usa;

-- Create a table
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256),
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES cities(id)
);