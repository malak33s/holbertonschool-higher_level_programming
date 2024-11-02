-- Script qui crée la table id_not_null avec id par défaut à 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
