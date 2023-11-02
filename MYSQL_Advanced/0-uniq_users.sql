-- Check if the table exists and drop it if it does (to handle scenarios where the table already exists)
DROP TABLE IF EXISTS users;

-- Create the "users" table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
