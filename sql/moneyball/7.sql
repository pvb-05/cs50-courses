SELECT "players"."first_name", "players"."last_name"
FROM "players"
JOIN "salaries" ON "players"."id" = "salaries"."player_id"
GROUP BY "salaries"."player_id"
ORDER BY MAX("salaries"."salary") DESC
LIMIT 1;

