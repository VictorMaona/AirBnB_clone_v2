-- Create or ensure the existence of the project database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or ensure the existence of the project user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant full privileges on the project database to the project user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema to the project user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
