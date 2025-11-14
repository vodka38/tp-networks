USE mydb;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT IGNORE INTO users (name, email) VALUES
('Tien', 'tien@exemple.com'),
('Sylvain', 'sylvain@clever.fr'),
('Docker', 'docker@hub.com');
