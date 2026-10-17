SELECT "salaries"."salary"
FROM "performances"
JOIN "salaries" ON "performances"."player_id" = "salaries"."player_id"
WHERE "salaries"."year" = 2001 AND "performances"."year" = 2001
GROUP BY "performances"."player_id"
ORDER BY MAX("performances"."HR") DESC
LIMIT 1;

