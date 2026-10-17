SELECT COUNT(print_number) AS number_of_prints
FROM views
WHERE english_title LIKE '%Kanagawa%'
ORDER BY english_title;
