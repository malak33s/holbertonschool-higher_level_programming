-- Lister les enregistrements avec un score >= 10, triés par score
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
