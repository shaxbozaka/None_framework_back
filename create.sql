CREATE DATABASE mds;


CREATE USER ‘python’@’localhost’ IDENTIFIED BY ‘blog.carlesmateo.com-db-password’;
CREATE USER ‘python’@’%’ IDENTIFIED BY ‘Qwerty123$’;
GRANT ALL PRIVILEGES ON carles_database.* TO ‘python’@’localhost’;
GRANT ALL PRIVILEGES ON carles_database.* TO ‘python’@’%’;


USE carles_database;

CREATE TABLE
    mds.customers (pk INT AUTO_INCREMENT PRIMARY KEY, group_code VARCHAR(15), group_desc VARCHAR(250), code VARCHAR(15), code_desc TEXT)
