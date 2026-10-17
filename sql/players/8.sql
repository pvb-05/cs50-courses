SELECT ROUND(AVG(weight),2) AS "Average weight", ROUND(AVG(height),2) AS "Average height"
FROM "players"
WHERE "debut" >= '2000-01-01';
