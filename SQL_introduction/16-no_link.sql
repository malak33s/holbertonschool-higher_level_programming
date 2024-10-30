-- Lister les enregistrements avec un nom (sans valeur nulle)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
