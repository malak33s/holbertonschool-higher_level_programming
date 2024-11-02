-- Crée la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilise la base de données
USE hbtn_0d_usa;

-- Crée la table `cities` si elle n'existe pas
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- ID unique et clé primaire
    state_id INT NOT NULL,               -- ID de l'état, obligatoire
    name VARCHAR(256) NOT NULL,          -- Nom de la ville, obligatoire
    FOREIGN KEY (state_id) REFERENCES states(id)  -- Clé étrangère vers `states`
);
