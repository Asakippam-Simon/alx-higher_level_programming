-- displays the max temperature of each state (ordered by State name)
-- Holberto School
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY MAX(value) DESC LIMIT 3;
