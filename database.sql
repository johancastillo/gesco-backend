/* Dalete Data Base if exists */
DROP DATABASE IF EXISTS monitor;

/* Create Data Base */
CREATE DATABASE monitor;
USE monitor;

/* Definition of the table contacts */
CREATE TABLE providers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rif VARCHAR(255),
    fullname VARCHAR(255),
    contributor VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255)
);

/* Inserting data in the table */
INSERT INTO providers (rif, fullname, contributor, phone, email) 
VALUES ("123456","Jc Johan", "Ordinario", "123456", "jcjohan2707@gmail.com"),
        ("545232", "Keymar Pérez", "Especial", "0415555", "test@gmail.com");

/* Validations */
SHOW TABLES;
SELECT * FROM providers;