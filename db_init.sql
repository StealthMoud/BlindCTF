CREATE DATABASE IF NOT EXISTS blind_ctf;
USE blind_ctf;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO users (username, password) VALUES ('admin', 'adminpassword');
