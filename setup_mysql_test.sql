-- Set up MySQL Test server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Ensure the existence of the test user or create if not exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the test database to the test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the performance_schema to the test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
