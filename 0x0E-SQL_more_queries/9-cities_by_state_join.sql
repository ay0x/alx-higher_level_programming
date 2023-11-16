-- Join Cities and States
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states on cities.id = states.id
ORDER BY cities.id ASC;