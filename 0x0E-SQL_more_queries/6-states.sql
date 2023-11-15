-- Create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to databse
USE hbtn_0d_usa;

-- Create a table
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY states(id)
);