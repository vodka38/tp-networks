-- Crée la base si elle n'existe pas (même si MYSQL_DATABASE est défini)
CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

-- Crée la table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Insère des données de test
INSERT INTO users (name, email) VALUES
('Tien', 'tien@example.com'),
('Sylvain', 'sylvain@clever.fr'),
('Docker', 'docker@hub.com');
